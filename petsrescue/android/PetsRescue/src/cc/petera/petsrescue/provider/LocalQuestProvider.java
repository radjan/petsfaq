package cc.petera.petsrescue.provider;

import java.util.ArrayList;

import android.util.SparseArray;
import cc.petera.petsrescue.data.Quest;
import cc.petera.petsrescue.data.SearchFilter;

/** Store quests in memory for test. */
public class LocalQuestProvider extends QuestProvider {

    static class CreateQuestFinishedRunnable implements Runnable {
        CreateQuestListener mListener;
        Quest mQuest;

        public CreateQuestFinishedRunnable(CreateQuestListener listener, Quest quest) {
            mListener = listener;
            mQuest = quest;
        }
        @Override
        public void run() {
            mListener.onFinished(true, mQuest);
        }
    }

    static class UpdateQuestFinishedRunnable implements Runnable {
        UpdateQuestListener mListener;
        Quest mQuest;

        public UpdateQuestFinishedRunnable(UpdateQuestListener listener, Quest quest) {
            mListener = listener;
            mQuest = quest;
        }
        @Override
        public void run() {
            mListener.onFinished(true, mQuest);
        }
    }

    static class SearchQuestFinishedRunnable implements Runnable {
        SearchQuestListener mListener;
        ArrayList<Quest> mResults;

        public SearchQuestFinishedRunnable(SearchQuestListener listener, ArrayList<Quest> results) {
            mListener = listener;
            mResults = results;
        }

        @Override
        public void run() {
            mListener.onFinished(mResults);
        }
    }

    long mNextId = 0;
    SparseArray<Quest> mQuests = new SparseArray<Quest>();

    @Override
    public void createQuest(Quest quest, CreateQuestListener listener) {
        quest.id = getNewId();
        mQuests.put((int) quest.id, quest);
        listener.getHandler().post(new CreateQuestFinishedRunnable(listener, quest));
        broadcastQuestUpdated();
    }

    @Override
    public void updateQuest(Quest quest, UpdateQuestListener listener) {
        mQuests.put((int) quest.id, quest);
        listener.getHandler().post(new UpdateQuestFinishedRunnable(listener, quest));
        broadcastQuestUpdated();
    }

    @Override
    public void searchQuest(SearchFilter filter, SearchQuestListener listener) {
        ArrayList<Quest> results = new ArrayList<Quest>();
        for (int i = 0; i < mQuests.size(); i++) {
            Quest quest = mQuests.valueAt(i);
            if (filter.filter(quest)) {
                results.add(quest);
            }
        }

        listener.getHandler().post(new SearchQuestFinishedRunnable(listener, results));
    }

    long getNewId() {
        mNextId++;
        return mNextId;
    }
}
