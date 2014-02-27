package cc.petera.petsrescue;

import java.util.Arrays;

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
import cc.petera.petsrescue.data.Animal;
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.fragment.AboutFragment;
import cc.petera.petsrescue.fragment.AnimalListFragment;
import cc.petera.petsrescue.fragment.EditMissionFragment;
import cc.petera.petsrescue.fragment.MainMenuFragment;
import cc.petera.petsrescue.fragment.MissionDetailFragment;
import cc.petera.petsrescue.fragment.MissionPagerFragment;
import cc.petera.petsrescue.provider.CloudMissionProvider;
import cc.petera.petsrescue.provider.ContextProvider;
import cc.petera.petsrescue.provider.MissionProvider;
import cc.petera.petsrescue.util.KeyHash;

import com.facebook.Request;
import com.facebook.Response;
import com.facebook.Session;
import com.facebook.SessionState;
import com.facebook.model.GraphUser;
import com.facebook.widget.UserSettingsFragment;

public class MainActivity extends FragmentActivity {
    private static final String TAG = "MainActivity";

    public static final String TAG_NEW_MISSION = "NEW_MISSION";
    public static final String TAG_MISSION_PAGER = "MISSION_PAGER";
    public static final String TAG_MISSION_DETAIL = "MISSION_DETAIL";
    public static final String TAG_ANIMAL_LIST = "ANIMAL_LIST";
    public static final String TAG_ABOUT = "ABOUT";

    public static final int REQUEST_PICK_PHOTO = 1;

    public interface ActivityResultListener {
        void onActivityResult(int resultCode, Intent returnedIntent);
    }

    Handler mHandler = new Handler();
    MissionProvider mMissionProvider;
    MainMenuFragment mMainMenuFragment;
    EditMissionFragment mNewMissionFragment;
    MissionPagerFragment mMissionPagerFragment;
    MissionDetailFragment mMissionDetailFragment;
    EditMissionFragment mEditMissionFragment;
    AnimalListFragment mAnimalListFragment;
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

    ContextProvider mContextProvider = new ContextProvider() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public Context getContext() {
            return MainActivity.this;
        }
        @Override
        public String getToken() {
            return mToken;
        }
    };

    MissionProvider.Observer mQuestObserver = new MissionProvider.Observer() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onMissionUpdated() {
            mMissionPagerFragment.refresh();
        }
    };

    MissionProvider.FacebookLoginListener mFacebookLoginListener = new MissionProvider.FacebookLoginListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished(String token) {
            mToken = token;
            showFacebookLoginFragment(false);
        }
    };

    MissionProvider.LogoutListener mLogoutListener = new MissionProvider.LogoutListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished() {
        }
    };

    MissionProvider.CreateMissionListener mCreateMissionListener = new MissionProvider.CreateMissionListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished(boolean success, Mission mission) {
            if (success) {
                //TODO:
            }
            else {
                //TODO:
            }
        }
    };

    MissionProvider.UpdateMissionListener mUpdateMissionListener = new MissionProvider.UpdateMissionListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished(boolean success, Mission mission) {
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

        mMissionProvider = new CloudMissionProvider();
        mMissionProvider.addObserver(mQuestObserver);

        mPetTypeArray = getResources().getStringArray(R.array.pet_type);
        mCatSubtypeArray = getResources().getStringArray(R.array.pet_subtype_cat);
        mDogSubtypeArray = getResources().getStringArray(R.array.pet_subtype_dog);
        mPetHealthArray = getResources().getStringArray(R.array.pet_health);

        createFragments();

        Log.d(TAG, "keyhash: " + KeyHash.getKeyHash(this, "cc.petera.petsrescue"));
        mUserSettingsFragment = (UserSettingsFragment) this.getSupportFragmentManager().findFragmentById(R.id.fragment_login);
        mUserSettingsFragment.setSessionStatusCallback(mSessionStatusCallback);
        mUserSettingsFragment.setReadPermissions(Arrays.asList("email", "user_birthday"));
    }

    @Override
    protected void onDestroy() {
        mMissionProvider.removeObserver(mQuestObserver);
        mMissionProvider.logout(mToken, mLogoutListener);
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

    public MissionProvider getMissionProvider() {
        return mMissionProvider;
    }

    public String getToken() {
        return mToken;
    }

    public long getUserId() {
        //TODO:
        return 1;
    }

    public void showNewMissionPage() {
        pushFragment(mNewMissionFragment, TAG_NEW_MISSION);
    }

    public void showMissionPagerPage(int tab) {
        mMissionPagerFragment.setDefaultTab(tab);
        pushFragment(mMissionPagerFragment, TAG_MISSION_PAGER);
    }

    public void showMissionDetailPage(Mission mission) {
        mMissionDetailFragment.setMission(mission);
        pushFragment(mMissionDetailFragment, TAG_MISSION_DETAIL);
    }

    public void showEditMissionPage(Mission mission) {
        mEditMissionFragment.setMission(mission);
        pushFragment(mEditMissionFragment, TAG_MISSION_DETAIL);
    }

    public void showAnimalListPage() {
        pushFragment(mAnimalListFragment, TAG_ANIMAL_LIST);
    }

    public void showAnimalDetailPage(Animal animal) {
        //TODO:
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

    public void startMission(Mission mission) {
        //TODO:
    }

    public void cancelMission(Mission mission) {
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
        mNewMissionFragment = new EditMissionFragment();
        mNewMissionFragment.setListener(new EditMissionFragment.Listener() {
            @Override
            public void onCancel(EditMissionFragment fragment) {
                popFragment(fragment);
            }
            @Override
            public void onOK(EditMissionFragment fragment, Mission mission) {
                mMissionProvider.createMission(mission, mCreateMissionListener);
                popFragment(fragment);
                showMissionPagerPage(MissionPagerFragment.TAB_AVAILABLE);
            }
        });

        mEditMissionFragment = new EditMissionFragment();
        mEditMissionFragment.setListener(new EditMissionFragment.Listener() {
            @Override
            public void onCancel(EditMissionFragment fragment) {
                popFragment(fragment);
            }
            @Override
            public void onOK(EditMissionFragment fragment, Mission mission) {
                mMissionProvider.updateMission(mission, mUpdateMissionListener);
                popFragment(fragment);
                mMissionDetailFragment.setMission(mission);
            }
        });

        mMissionPagerFragment = new MissionPagerFragment();
        mMissionDetailFragment = new MissionDetailFragment();
        mAnimalListFragment = new AnimalListFragment();
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
            Request meRequest = Request.newMeRequest(session, new Request.GraphUserCallback() {
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

                    mMissionProvider.facebookLogin(user.getId(), session.getAccessToken(), mFacebookLoginListener);
                }
            });
            meRequest.executeAsync();
        }
    }
}
