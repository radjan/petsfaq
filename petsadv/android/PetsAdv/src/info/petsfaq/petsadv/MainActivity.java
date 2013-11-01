package info.petsfaq.petsadv;

import info.petsfaq.petsadv.util.KeyHash;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.util.Log;
import android.view.Menu;

import com.facebook.Request;
import com.facebook.Response;
import com.facebook.Session;
import com.facebook.SessionState;
import com.facebook.model.GraphUser;
import com.facebook.widget.UserSettingsFragment;

public class MainActivity extends FragmentActivity {
    private static final String TAG = "MainActivity";

    /** Facebook login fragment. */
    UserSettingsFragment mUserSettingsFragment;

    Session.StatusCallback mSessionStatusCallback = new Session.StatusCallback() {
        @Override
        public void call(Session session, SessionState state, Exception exception) {
            onSessionStateChange(session, state, exception);
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d(TAG, "keyhash=" + KeyHash.getKeyHash(this, "info.petsfaq.petsadv"));

        mUserSettingsFragment = (UserSettingsFragment) this.getSupportFragmentManager().findFragmentById(R.id.fragment_login);
        mUserSettingsFragment.setSessionStatusCallback(mSessionStatusCallback);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    void onSessionStateChange(Session session, SessionState state, Exception exception) {
        FragmentManager fm = this.getSupportFragmentManager();
        if (session.isClosed()) {
            FragmentTransaction action = fm.beginTransaction();
            action.show(mUserSettingsFragment);
            action.commitAllowingStateLoss();
        }
        else {
            FragmentTransaction action = fm.beginTransaction();
            action.hide(mUserSettingsFragment);
            action.commitAllowingStateLoss();

            Request.executeMeRequestAsync(session, new Request.GraphUserCallback() {
                @Override
                public void onCompleted(GraphUser user, Response response) {
                    Log.d(TAG, "executeMeRequestAsync response=" + response);

                    if (user == null) {
                        Log.d(TAG, "user invalid");
                    }
                    else {
                        Log.d(TAG, "id=" + user.getId());
                    }

                    Session session = Session.getActiveSession();
                    if (null == session || !session.isOpened()) {
                        Log.d(TAG, "session invalid");
                    }
                    else {
                        Log.d(TAG, "token=" + session.getAccessToken());
                    }
                }
            });
        }
    }
}
