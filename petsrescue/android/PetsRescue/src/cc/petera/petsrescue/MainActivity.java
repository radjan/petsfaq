package cc.petera.petsrescue;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;
import cc.petera.petsrescue.data.Quest;
import cc.petera.petsrescue.fragment.AboutFragment;
import cc.petera.petsrescue.fragment.EditQuestFragment;
import cc.petera.petsrescue.fragment.MainMenuFragment;
import cc.petera.petsrescue.fragment.QuestDetailFragment;
import cc.petera.petsrescue.fragment.QuestPagerFragment;
import cc.petera.petsrescue.provider.LocalQuestProvider;
import cc.petera.petsrescue.provider.QuestProvider;
import cc.petera.petsrescue.util.KeyHash;

import com.facebook.Request;
import com.facebook.Response;
import com.facebook.Session;
import com.facebook.SessionState;
import com.facebook.model.GraphUser;
import com.facebook.widget.UserSettingsFragment;

public class MainActivity extends FragmentActivity {
    private static final String TAG = "MainActivity";

    public static final String TAG_NEW_QUEST = "NEW_QUEST";
    public static final String TAG_QUEST_PAGER = "QUEST_PAGER";
    public static final String TAG_QUEST_DETAIL = "QUEST_DETAIL";
    public static final String TAG_ABOUT = "ABOUT";

    public static final int REQUEST_PICK_PHOTO = 1;

    public enum Page {
        NEW_QUEST,
        QUEST_PAGER,
        ABOUT,
    }

    public interface ActivityResultListener {
        void onActivityResult(int resultCode, Intent returnedIntent);
    }

    class FacebookLoginRunnable implements Runnable {
        String mFacebookId;
        String mFacebookToken;
        public FacebookLoginRunnable(String id, String token) {
            mFacebookId = id;
            mFacebookToken = token;
        }

        @Override
        public void run() {
            if (null == mFacebookId || 0 == mFacebookId.length() ||
                    null == mFacebookToken || 0 == mFacebookToken.length()) {
                return;
            }

            HttpClient httpClient = new DefaultHttpClient();
            HttpPost httpPost = new HttpPost("http://www.petsfaq.info:6543/m/login/facebook");

            try {
                List<NameValuePair> params = new ArrayList<NameValuePair>(2);
                params.add(new BasicNameValuePair("fb_id", mFacebookId));
                params.add(new BasicNameValuePair("fb_access_token", mFacebookToken));
                httpPost.setEntity(new UrlEncodedFormEntity(params));
                HttpResponse response = httpClient.execute(httpPost);
                if (null == response) {
                    Log.d(TAG, "Login response=null");
                    return;
                }
                int statusCode = response.getStatusLine().getStatusCode();
                if (statusCode != 200) {
                    Log.d(TAG, "Login response status-code=" + statusCode);
                    return;
                }
                JSONObject responseJson = new JSONObject(EntityUtils.toString(response.getEntity()));
                JSONObject responseData = responseJson.getJSONObject("data");
                if (null == responseData) {
                    Log.d(TAG, "Login response data=" + null);
                    return;
                }
                mToken = responseData.getString("token");
            }
            catch (ClientProtocolException e) {
            }
            catch (IOException e) {
            }
            catch (JSONException e) {
            }

            showFacebookLoginFragment(false);
        }
    }

    class LogoutRunnable implements Runnable {
        String mLogoutToken;
        public LogoutRunnable(String token) {
            mLogoutToken = token;
        }

        @Override
        public void run() {
            if (null == mLogoutToken || 0 == mLogoutToken.length()) {
                return;
            }

            HttpClient httpClient = new DefaultHttpClient();
            //TODO: url encode?
            HttpDelete httpDelete = new HttpDelete("http://www.petsfaq.info:6543/m/logout?token=" + mLogoutToken);

            try {
                httpClient.execute(httpDelete);
            } catch (ClientProtocolException e) {
                Log.d(TAG, e.toString());
            } catch (IOException e) {
                Log.d(TAG, e.toString());
            }
        }
    };

    Handler mHandler = new Handler();
    QuestProvider mQuestProvider;
    MainMenuFragment mMainMenuFragment;
    EditQuestFragment mNewQuestFragment;
    QuestPagerFragment mQuestPagerFragment;
    QuestDetailFragment mQuestDetailFragment;
    EditQuestFragment mEditQuestFragment;
    AboutFragment mAboutFragment;

    ActivityResultListener mPickPhotoListener;
    String[] mPetTypeArray;
    String[] mCatSubtypeArray;
    String[] mDogSubtypeArray;
    String[] mPetHealthArray;

    String mToken;
    UserSettingsFragment mUserSettingsFragment;

    Session.StatusCallback mSessionStatusCallback = new Session.StatusCallback() {
        @Override
        public void call(Session session, SessionState state, Exception exception) {
            onSessionStateChange(session, state, exception);
        }
    };

    QuestProvider.Observer mQuestObserver = new QuestProvider.Observer() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public void onQuestUpdated() {
            mQuestPagerFragment.refresh();
        }
    };

    QuestProvider.CreateQuestListener mCreateQuestListener = new QuestProvider.CreateQuestListener() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public Context getContext() {
            return MainActivity.this;
        }
        @Override
        public void onFinished(boolean success, Quest quest) {
            if (success) {
                //TODO:
            }
            else {
                //TODO:
            }
        }
    };

    QuestProvider.UpdateQuestListener mUpdateQuestListener = new QuestProvider.UpdateQuestListener() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public Context getContext() {
            return MainActivity.this;
        }
        @Override
        public void onFinished(boolean success, Quest quest) {
            if (success) {
                //TODO:
            }
            else {
                //TODO:
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FragmentManager fm = this.getSupportFragmentManager();
        mMainMenuFragment = (MainMenuFragment) fm.findFragmentById(R.id.fragment_main_menu);

        mQuestProvider = new LocalQuestProvider();
        mQuestProvider.addObserver(mQuestObserver);

        mPetTypeArray = getResources().getStringArray(R.array.pet_type);
        mCatSubtypeArray = getResources().getStringArray(R.array.pet_subtype_cat);
        mDogSubtypeArray = getResources().getStringArray(R.array.pet_subtype_dog);
        mPetHealthArray = getResources().getStringArray(R.array.pet_health);

        createFragments();

        Log.d(TAG, "keyhash: " + KeyHash.getKeyHash(this, "cc.petera.petsrescue"));
        mUserSettingsFragment = (UserSettingsFragment) this.getSupportFragmentManager().findFragmentById(R.id.fragment_login);
        mUserSettingsFragment.setSessionStatusCallback(mSessionStatusCallback);
    }

    @Override
    protected void onDestroy() {
        mQuestProvider.removeObserver(mQuestObserver);
        logout(mToken);
        super.onDestroy();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
        case R.id.action_about:
            showAboutPage();
            return true;
        }
        return false;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent returnedIntent) {
        super.onActivityResult(requestCode, resultCode, returnedIntent);

        switch(requestCode) {
        case REQUEST_PICK_PHOTO:
            mPickPhotoListener.onActivityResult(resultCode, returnedIntent);
        }
    }

    public QuestProvider getQuestProvider() {
        return mQuestProvider;
    }

    public long getOwnerId() {
        //TODO:
        return 1;
    }

    public void showNewQuestPage() {
        pushFragment(mNewQuestFragment, TAG_NEW_QUEST);
    }

    public void showQuestPagerPage(int tab) {
        mQuestPagerFragment.setDefaultTab(tab);
        pushFragment(mQuestPagerFragment, TAG_QUEST_PAGER);
    }

    public void showQuestDetailPage(Quest quest) {
        mQuestDetailFragment.setQuest(quest);
        pushFragment(mQuestDetailFragment, TAG_QUEST_DETAIL);
    }

    public void showEditQuestPage(Quest quest) {
        mEditQuestFragment.setQuest(quest);
        pushFragment(mEditQuestFragment, TAG_QUEST_DETAIL);
    }

    public void showAboutPage() {
        pushFragment(mAboutFragment, TAG_ABOUT);
    }

    public String getPetTypeString(int type) {
        return mPetTypeArray[type];
    }

    public int getPetSubtypeArrayId(int type) {
        switch (type) {
        case 0:
            return R.array.pet_subtype_cat;
        case 1:
            return R.array.pet_subtype_dog;
        }
        return 0;
    }

    public String getPetSubtypeString(int type, int subtype) {
        switch (type) {
        case 0:
            return mCatSubtypeArray[subtype];
        case 1:
            return mDogSubtypeArray[subtype];
        }
        return "";
    }

    public String getPetHealthString(int health) {
        return mPetHealthArray[health];
    }

    public void pickPhoto(ActivityResultListener listener) {
        mPickPhotoListener = listener;
        Intent intent = new Intent(Intent.ACTION_PICK);
        intent.setType("image/*");
        startActivityForResult(intent, REQUEST_PICK_PHOTO);
    }

    public void startQuest(Quest quest) {
        //TODO:
    }

    public void cancelQuest(Quest quest) {
        //TODO:
    }

    void pushFragment(Fragment fragment, String tag) {
        FragmentTransaction ft = this.getSupportFragmentManager().beginTransaction();
        ft.add(R.id.fragment_container, fragment);
        ft.addToBackStack(tag);
        ft.commit();
    }

    void popFragment(Fragment fragment) {
        FragmentTransaction ft = this.getSupportFragmentManager().beginTransaction();
        ft.remove(fragment);
        ft.commit();
    }

    void createFragments() {
        mNewQuestFragment = new EditQuestFragment();
        mNewQuestFragment.setListener(new EditQuestFragment.Listener() {
            @Override
            public void onCancel(EditQuestFragment fragment) {
                popFragment(fragment);
            }
            @Override
            public void onOK(EditQuestFragment fragment, Quest quest) {
                mQuestProvider.createQuest(quest, mCreateQuestListener);
                popFragment(fragment);
                showQuestPagerPage(QuestPagerFragment.TAB_AVAILABLE);
            }
        });

        mEditQuestFragment = new EditQuestFragment();
        mEditQuestFragment.setListener(new EditQuestFragment.Listener() {
            @Override
            public void onCancel(EditQuestFragment fragment) {
                popFragment(fragment);
            }
            @Override
            public void onOK(EditQuestFragment fragment, Quest quest) {
                mQuestProvider.updateQuest(quest, mUpdateQuestListener);
                popFragment(fragment);
                mQuestDetailFragment.setQuest(quest);
            }
        });

        mQuestPagerFragment = new QuestPagerFragment();
        mQuestDetailFragment = new QuestDetailFragment();
        mAboutFragment = new AboutFragment();
    }

    void showFacebookLoginFragment(boolean show) {
        FragmentManager fm = this.getSupportFragmentManager();
        FragmentTransaction action = fm.beginTransaction();
        if (show) {
            action.show(mUserSettingsFragment);
        }
        else {
            action.hide(mUserSettingsFragment);
        }
        action.commitAllowingStateLoss();
    }

    void onSessionStateChange(Session session, SessionState state, Exception exception) {
        if (!session.isOpened()) {
            showFacebookLoginFragment(true);
            if (SessionState.CLOSED_LOGIN_FAILED == state) {
                Toast toast = Toast.makeText(this, R.string.toast_facebook_login_failed, Toast.LENGTH_LONG);
                toast.show();
            }
        }
        else {
            Request.newMeRequest(session, new Request.GraphUserCallback() {
                @Override
                public void onCompleted(GraphUser user, Response response) {
                    if (user == null) {
                        Log.d(TAG, "user invalid");
                        return;
                    }

                    Session session = Session.getActiveSession();
                    if (null == session || !session.isOpened()) {
                        Log.d(TAG, "session invalid");
                        return;
                    }

                    login(user.getId(), session.getAccessToken());
                }
            }).executeAsync();
        }
    }

    void login(String id, String token) {
        Thread thread = new Thread(new FacebookLoginRunnable(id, token));
        thread.start();
    }

    void logout(String token) {
        Thread thread = new Thread(new LogoutRunnable(token));
        thread.start();
    }
}
