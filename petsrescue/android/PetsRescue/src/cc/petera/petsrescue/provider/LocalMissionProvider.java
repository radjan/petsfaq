package cc.petera.petsrescue.provider;

import java.util.ArrayList;

import android.util.SparseArray;
import cc.petera.petsrescue.data.Animal;
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.data.SearchAnimalFilter;
import cc.petera.petsrescue.data.SearchMissionFilter;

/** Store Missions in memory for test. */
public class LocalMissionProvider extends MissionProvider {

    static class FacebookLoginFinishedRunnable implements Runnable {
        FacebookLoginListener mListener;

        public FacebookLoginFinishedRunnable(FacebookLoginListener listener) {
            mListener = listener;
        }
        @Override
        public void run() {
            mListener.onFinished("dummy");
        }
    }

    static class LogoutFinishedRunnable implements Runnable {
        LogoutListener mListener;

        public LogoutFinishedRunnable(LogoutListener listener) {
            mListener = listener;
        }
        @Override
        public void run() {
            mListener.onFinished();
        }
    }

    static class CreateMissionFinishedRunnable implements Runnable {
        CreateMissionListener mListener;
        Mission mMission;

        public CreateMissionFinishedRunnable(CreateMissionListener listener, Mission mission) {
            mListener = listener;
            mMission = mission;
        }
        @Override
        public void run() {
            mListener.onFinished(true, mMission);
        }
    }

    static class UpdateMissionFinishedRunnable implements Runnable {
        UpdateMissionListener mListener;
        Mission mMission;

        public UpdateMissionFinishedRunnable(UpdateMissionListener listener, Mission mission) {
            mListener = listener;
            mMission = mission;
        }
        @Override
        public void run() {
            mListener.onFinished(true, mMission);
        }
    }

    static class SearchMissionFinishedRunnable implements Runnable {
        SearchMissionListener mListener;
        ArrayList<Mission> mResults;

        public SearchMissionFinishedRunnable(SearchMissionListener listener, ArrayList<Mission> results) {
            mListener = listener;
            mResults = results;
        }

        @Override
        public void run() {
            mListener.onFinished(mResults);
        }
    }

    static class SearchAnimalFinishedRunnable implements Runnable {
        SearchAnimalListener mListener;
        ArrayList<Animal> mResults;

        public SearchAnimalFinishedRunnable(SearchAnimalListener listener, ArrayList<Animal> results) {
            mListener = listener;
            mResults = results;
        }

        @Override
        public void run() {
            mListener.onFinished(mResults);
        }
    }

    long mNextId = 0;
    SparseArray<Mission> mMissions = new SparseArray<Mission>();
    SparseArray<Animal> mAnimals = new SparseArray<Animal>();

    @Override
    public void facebookLogin(String fbId, String fbToken, FacebookLoginListener listener) {
        listener.getContextProvider().getHandler().post(new FacebookLoginFinishedRunnable(listener));
    }
    @Override
    public void logout(String token, LogoutListener listener) {
        listener.getContextProvider().getHandler().post(new LogoutFinishedRunnable(listener));
    }

    @Override
    public void createMission(Mission mission, CreateMissionListener listener) {
        mission.id = getNewId();
        mMissions.put((int) mission.id, mission);
        listener.getContextProvider().getHandler().post(new CreateMissionFinishedRunnable(listener, mission));
        broadcastMissionUpdated();
    }

    @Override
    public void updateMission(Mission mission, UpdateMissionListener listener) {
        mMissions.put((int) mission.id, mission);
        listener.getContextProvider().getHandler().post(new UpdateMissionFinishedRunnable(listener, mission));
        broadcastMissionUpdated();
    }

    @Override
    public void searchMission(SearchMissionFilter filter, SearchMissionListener listener) {
        ArrayList<Mission> results = new ArrayList<Mission>();
        for (int i = 0; i < mMissions.size(); i++) {
            Mission mission = mMissions.valueAt(i);
            if (filter.filter(mission)) {
                results.add(mission);
            }
        }

        listener.getContextProvider().getHandler().post(new SearchMissionFinishedRunnable(listener, results));
    }

    @Override
    public void searchAnimal(SearchAnimalFilter filter, SearchAnimalListener listener) {
        ArrayList<Animal> results = new ArrayList<Animal>();
        for (int i = 0; i < mAnimals.size(); i++) {
            Animal animal = mAnimals.valueAt(i);
            if (filter.filter(animal)) {
                results.add(animal);
            }
        }
        listener.getContextProvider().getHandler().post(new SearchAnimalFinishedRunnable(listener, results));
    }

    long getNewId() {
        mNextId++;
        return mNextId;
    }
}
