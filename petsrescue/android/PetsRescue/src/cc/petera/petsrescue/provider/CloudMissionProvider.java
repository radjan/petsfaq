package cc.petera.petsrescue.provider;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

import android.util.Log;
import cc.petera.petsrescue.data.Animal;
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.data.SearchFilter;

public class CloudMissionProvider extends MissionProvider {
    private static final String TAG = "CloudMissionProvider";

    public static final String URI_PREFIX = "http://www.petsfaq.info:6543/m";
    public static final String URI_FACEBOOK_LOGIN = URI_PREFIX + "/login/facebook";
    public static final String URI_LOGOUT = URI_PREFIX + "/logout";
    public static final String API_PREFIX = "http://www.petsfaq.info:6543/api/v1";
    public static final String API_CREATE_MISSION = API_PREFIX + "/missions";
    public static final String API_LIST_MISSION = API_PREFIX + "/missions";
    public static final String API_CREATE_ANIMAL = API_PREFIX + "/animals";

    class FacebookLoginRunnable implements Runnable {
        class FinishedRunnable implements Runnable {
            @Override
            public void run() {
                mListener.onFinished(mToken);
            }
        }

        String mFacebookId;
        String mFacebookToken;
        FacebookLoginListener mListener;
        String mToken = null;

        public FacebookLoginRunnable(String id, String token, FacebookLoginListener listener) {
            mFacebookId = id;
            mFacebookToken = token;
            mListener = listener;
        }

        @Override
        public void run() {
            mToken = facebookLogin(mFacebookId, mFacebookToken);
            mListener.getContextProvider().getHandler().post(new FinishedRunnable());
        }
    }

    class LogoutRunnable implements Runnable {
        class FinishedRunnable implements Runnable {
            @Override
            public void run() {
                mListener.onFinished();
            }
        }

        String mLogoutToken;
        LogoutListener mListener;

        public LogoutRunnable(String token, LogoutListener listener) {
            mLogoutToken = token;
            mListener = listener;
        }

        @Override
        public void run() {
            logout(mLogoutToken);
            mListener.getContextProvider().getHandler().post(new FinishedRunnable());
        }
    };

    class CreateMissionRunnable implements Runnable {
        class FinishedRunnable implements Runnable {
            @Override
            public void run() {
                mListener.onFinished((INVALID_ID != mMission.id), mMission);
                broadcastMissionUpdated();
            }
        }

        Mission mMission;
        CreateMissionListener mListener;

        public CreateMissionRunnable(Mission mission, CreateMissionListener listener) {
            mMission = mission;
            mListener = listener;
        }

        @Override
        public void run() {
            createMission(mListener.getContextProvider().getToken(), mMission);
            mListener.getContextProvider().getHandler().post(new FinishedRunnable());
        }
    };

    class UpdateMissionRunnable implements Runnable {
        class FinishedRunnable implements Runnable {
            @Override
            public void run() {
                mListener.onFinished(false, mMission);
                broadcastMissionUpdated();
            }
        }

        Mission mMission;
        UpdateMissionListener mListener;

        public UpdateMissionRunnable(Mission mission, UpdateMissionListener listener) {
            mMission = mission;
            mListener = listener;
        }

        @Override
        public void run() {
            //TODO:
            mListener.getContextProvider().getHandler().post(new FinishedRunnable());
        }
    };

    class SearchMissionRunnable implements Runnable {
        class FinishedRunnable implements Runnable {
            @Override
            public void run() {
                mListener.onFinished(mMissions);
                broadcastMissionUpdated();
            }
        }

        SearchFilter mFilter;
        SearchMissionListener mListener;
        ArrayList<Mission> mMissions = new ArrayList<Mission>();

        public SearchMissionRunnable(SearchFilter filter, SearchMissionListener listener) {
            mFilter = filter;
            mListener = listener;
        }

        @Override
        public void run() {
            //TODO:
            mListener.getContextProvider().getHandler().post(new FinishedRunnable());
        }
    };

    static ExecutorService sExecutor = Executors.newSingleThreadExecutor();

    String facebookLogin(String fbId, String fbToken) {
        if (null == fbId || 0 == fbId.length() ||
                null == fbToken || 0 == fbToken.length()) {
            return null;
        }

        HttpClient httpClient = new DefaultHttpClient();
        HttpPost httpPost = new HttpPost(CloudMissionProvider.URI_FACEBOOK_LOGIN);

        try {
            List<NameValuePair> params = new ArrayList<NameValuePair>(2);
            params.add(new BasicNameValuePair("fb_id", fbId));
            params.add(new BasicNameValuePair("fb_access_token", fbToken));
            httpPost.setEntity(new UrlEncodedFormEntity(params));
            HttpResponse response = httpClient.execute(httpPost);
            if (null == response) {
                Log.d(TAG, "Login response=null");
                return null;
            }
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode != 200) {
                Log.d(TAG, "Login response status-code=" + statusCode);
                return null;
            }
            JSONObject responseJson = new JSONObject(EntityUtils.toString(response.getEntity()));
            JSONObject responseData = responseJson.getJSONObject("data");
            if (null == responseData) {
                Log.d(TAG, "Login response data=null");
                return null;
            }
            return responseData.getString("token");
        }
        catch (ClientProtocolException e) {
        }
        catch (IOException e) {
        }
        catch (JSONException e) {
        }

        return null;
    }

    @Override
    public void facebookLogin(String fbId, String fbToken, FacebookLoginListener listener) {
        sExecutor.execute(new FacebookLoginRunnable(fbId, fbToken, listener));
    }

    void logout(String token) {
        if (null == token || 0 == token.length()) {
            return;
        }

        HttpClient httpClient = new DefaultHttpClient();
        //TODO: url encode?
        HttpDelete httpDelete = new HttpDelete(CloudMissionProvider.URI_LOGOUT + "?token=" + token);

        try {
            httpClient.execute(httpDelete);
        } catch (ClientProtocolException e) {
            Log.d(TAG, e.toString());
        } catch (IOException e) {
            Log.d(TAG, e.toString());
        }
    }

    @Override
    public void logout(String token, LogoutListener listener) {
        sExecutor.execute(new LogoutRunnable(token, listener));
    }

    void putId(JSONObject obj, String key, long id) throws JSONException {
        if (INVALID_ID != id) {
            obj.put(key, String.valueOf(id));
        }
    }

    long createAnimal(String token, Animal animal) {
        if (INVALID_ID != animal.id) {
            return INVALID_ID;
        }

        HttpClient httpClient = new DefaultHttpClient();
        //TODO: url encode?
        HttpPost httpPost = new HttpPost(API_CREATE_ANIMAL + "?token=" + token);

        //TODO:
        String status = "";

        try {
            JSONObject body = new JSONObject();
            body.put("name", animal.name);
            body.put("type", Animal.getTypeName(animal.type));
            body.put("sub_type", Animal.getSubtypeName(animal.type, animal.subtype));
            body.put("status", status);
            body.put("description", animal.description);
            putId(body, "owner_id", animal.owner_id);
            putId(body, "find_location_id", animal.find_location_id);
            putId(body, "current_location_id", animal.current_location_id);

            httpPost.setEntity(new StringEntity(body.toString(), "UTF8"));
            httpPost.setHeader("Content-type", "application/json");
            HttpResponse response = httpClient.execute(httpPost);
            if (null == response) {
                Log.d(TAG, "Create animal response=null");
                return INVALID_ID;
            }
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode != 200) {
                Log.d(TAG, "Create animal response status-code=" + statusCode);
                return INVALID_ID;
            }
            JSONObject responseJson = new JSONObject(EntityUtils.toString(response.getEntity()));
            JSONObject responseInfo = responseJson.getJSONObject("info");
            if (null == responseInfo) {
                Log.d(TAG, "Create animal response info=null");
                return INVALID_ID;
            }

            return responseInfo.getLong("id");
        }
        catch (ClientProtocolException e) {
        }
        catch (IOException e) {
        }
        catch (JSONException e) {
        }

        return INVALID_ID;
    }

    long createMission(String token, Mission mission) {
        if (INVALID_ID != mission.id) {
            return INVALID_ID;
        }

        long animal_id = createAnimal(token, mission.animal);
        if (MissionProvider.INVALID_ID == mission.animal.id) {
            return INVALID_ID;
        }
        else {
            mission.animal.id = animal_id;
        }

        HttpClient httpClient = new DefaultHttpClient();
        //TODO: url encode?
        HttpPost httpPost = new HttpPost(API_CREATE_MISSION + "?token=" + token);

        //TODO:
        String status = "";
        String due_time = null;

        try {
            JSONObject body = new JSONObject();
            body.put("name", mission.name);
            body.put("type", Mission.getTypeName(mission.type));
            body.put("status", status);
            body.put("place", mission.place);
            body.put("note", mission.note);
            body.put("due_time", due_time);
            body.put("completed", String.valueOf(mission.completed));
            putId(body, "animal_id", mission.animal.id);
            putId(body, "dest_location_id", mission.dest_location_id);
            putId(body, "host_id", mission.host_id);
            putId(body, "from_location_id", mission.from_location_id);
            body.put("requirement", mission.requirement);
            body.put("period", mission.period);
            body.put("skill", mission.skill);

            httpPost.setEntity(new StringEntity(body.toString(), "UTF8"));
            httpPost.setHeader("Content-type", "application/json");
            HttpResponse response = httpClient.execute(httpPost);
            if (null == response) {
                Log.d(TAG, "Create mission response=null");
                return INVALID_ID;
            }
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode != 200) {
                Log.d(TAG, "Create mission response status-code=" + statusCode);
                return INVALID_ID;
            }
            JSONObject responseJson = new JSONObject(EntityUtils.toString(response.getEntity()));
            JSONObject responseInfo = responseJson.getJSONObject("info");
            if (null == responseInfo) {
                Log.d(TAG, "Create mission response info=null");
                return INVALID_ID;
            }

            return responseInfo.getLong("id");
        }
        catch (ClientProtocolException e) {
        }
        catch (IOException e) {
        }
        catch (JSONException e) {
        }
        return INVALID_ID;
    }

    @Override
    public void createMission(Mission mission, CreateMissionListener listener) {
        sExecutor.execute(new CreateMissionRunnable(mission, listener));
    }

    @Override
    public void updateMission(Mission mission, UpdateMissionListener listener) {
        sExecutor.execute(new UpdateMissionRunnable(mission, listener));
    }

    @Override
    public void searchMission(SearchFilter filter, SearchMissionListener listener) {
        sExecutor.execute(new SearchMissionRunnable(filter, listener));
    }
}
