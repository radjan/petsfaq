package cc.petera.petsrescue.provider;

import java.util.ArrayList;

import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.data.SearchFilter;

public abstract class MissionProvider {

    public static final long INVALID_ID = -1;

    public enum SearchType {
        ONGOING,
        AVAILABLE,
        TRACKED,
        COMPLETED
    }

    public interface Observer {
        ContextProvider getContextProvider();
        void onMissionUpdated();
    }

    public interface FacebookLoginListener {
        ContextProvider getContextProvider();
        void onFinished(String token);
    }

    public interface LogoutListener {
        ContextProvider getContextProvider();
        void onFinished();
    }

    public interface CreateMissionListener {
        ContextProvider getContextProvider();
        void onFinished(boolean success, Mission Mission);
    }

    public interface UpdateMissionListener {
        ContextProvider getContextProvider();
        void onFinished(boolean success, Mission Mission);
    }

    public interface SearchMissionListener {
        ContextProvider getContextProvider();
        void onFinished(ArrayList<Mission> results);
    }

    static class MissionUpdatedRunnable implements Runnable {
        Observer mObserver;

        public MissionUpdatedRunnable(Observer observer) {
            mObserver = observer;
        }
        @Override
        public void run() {
            mObserver.onMissionUpdated();
        }
    }

    ArrayList<Observer> mObservers = new ArrayList<Observer>();

    public void addObserver(Observer observer) {
        mObservers.add(observer);
    }
    public void removeObserver(Observer observer) {
        mObservers.remove(observer);
    }
    void broadcastMissionUpdated() {
        for (Observer observer : mObservers) {
            observer.getContextProvider().getHandler().post(new MissionUpdatedRunnable(observer));
        }
    }
    public abstract void facebookLogin(String fbId, String fbToken, FacebookLoginListener listener);
    public abstract void logout(String token, LogoutListener listener);
    public abstract void createMission(Mission Mission, CreateMissionListener listener);
    public abstract void updateMission(Mission Mission, UpdateMissionListener listener);
    public abstract void searchMission(SearchFilter filter, SearchMissionListener listener);
}
