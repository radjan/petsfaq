package cc.petera.petsrescue.provider;

import java.util.ArrayList;

import android.content.Context;
import android.os.Handler;
import cc.petera.petsrescue.data.Quest;
import cc.petera.petsrescue.data.SearchFilter;

public abstract class QuestProvider {
    public enum SearchType {
        ONGOING,
        AVAILABLE,
        TRACKED,
        COMPLETED
    }

    public interface Observer {
        Handler getHandler();
        void onQuestUpdated();
    }

    public interface CreateQuestListener {
        Handler getHandler();
        Context getContext();
        void onFinished(boolean success, Quest quest);
    }

    public interface UpdateQuestListener {
        Handler getHandler();
        Context getContext();
        void onFinished(boolean success, Quest quest);
    }

    public interface SearchQuestListener {
        Handler getHandler();
        Context getContext();
        void onFinished(ArrayList<Quest> results);
    }

    static class QuestUpdatedRunnable implements Runnable {
        Observer mObserver;

        public QuestUpdatedRunnable(Observer observer) {
            mObserver = observer;
        }
        @Override
        public void run() {
            mObserver.onQuestUpdated();
        }
    }

    ArrayList<Observer> mObservers = new ArrayList<Observer>();

    public void addObserver(Observer observer) {
        mObservers.add(observer);
    }
    public void removeObserver(Observer observer) {
        mObservers.remove(observer);
    }
    void broadcastQuestUpdated() {
        for (Observer observer : mObservers) {
            observer.getHandler().post(new QuestUpdatedRunnable(observer));
        }
    }
    public abstract void createQuest(Quest quest, CreateQuestListener listener);
    public abstract void updateQuest(Quest quest, UpdateQuestListener listener);
    public abstract void searchQuest(SearchFilter filter, SearchQuestListener listener);
}
