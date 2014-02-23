package cc.petera.petsrescue.fragment;

import java.util.ArrayList;

import android.content.Context;
import android.content.res.Resources;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.ListFragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;
import cc.petera.petsrescue.data.Quest;
import cc.petera.petsrescue.data.SearchFilter;
import cc.petera.petsrescue.provider.QuestProvider;

public class QuestListFragment extends ListFragment {

    class QuestListAdapter extends BaseAdapter {
        @Override
        public int getCount() {
            return mQuests.size();
        }
        @Override
        public Object getItem(int position) {
            return mQuests.get(position);
        }
        @Override
        public long getItemId(int position) {
            return position;
        }
        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (null == convertView) {
                convertView = mInflater.inflate(R.layout.item_quest, null);
            }

            Quest quest = (Quest) getItem(position);

            LinearLayout itemLayout = (LinearLayout) convertView;
            TextView nameView = (TextView) itemLayout.findViewById(R.id.text_name);
            TextView typeView = (TextView) itemLayout.findViewById(R.id.text_type);
            nameView.setText(quest.pet.name);
            typeView.setText(getQuestTypeLabel(quest.type));

            return itemLayout;
        }
    }

    Handler mHandler = new Handler();
    LayoutInflater mInflater;
    QuestListAdapter mAdapter = new QuestListAdapter();
    SearchFilter mSearchFilter;
    ArrayList<Quest> mQuests = new ArrayList<Quest>();

    QuestProvider.SearchQuestListener mSearchQuestCompleteListener = new QuestProvider.SearchQuestListener() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public Context getContext() {
            return getActivity();
        }
        @Override
        public void onFinished(ArrayList<Quest> results) {
            mQuests = results;
            mAdapter.notifyDataSetChanged();
        }
    };

    @Override
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        this.setEmptyText(getActivity().getString(R.string.quest_list_empty));
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mInflater = LayoutInflater.from(this.getActivity());
        this.setListAdapter(mAdapter);
        refresh();
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        MainActivity mainActivity = (MainActivity) this.getActivity();
        Quest quest = (Quest) this.getListAdapter().getItem(position);
        mainActivity.showQuestDetailPage(quest);
    }

    public void setSearchFilter(SearchFilter searchFilter) {
        mSearchFilter = searchFilter;
        refresh();
    }

    public void refresh() {
        if (null == mSearchFilter || null == getActivity()) {
            return;
        }
        ((MainActivity) this.getActivity()).getQuestProvider().searchQuest(mSearchFilter, mSearchQuestCompleteListener);
    }

    String getQuestTypeLabel(Quest.Type type) {
        Resources res = this.getActivity().getResources();
        int stringId = 0;
        switch (type) {
        case CATCH:
           stringId = R.string.quest_type_catch;
           break;
        case TRANSPORT:
            stringId = R.string.quest_type_catch;
            break;
        case HALFWAY:
            stringId = R.string.quest_type_catch;
            break;
        case ADOPT:
            stringId = R.string.quest_type_catch;
            break;
        case DONATE:
            stringId = R.string.quest_type_catch;
            break;
        }
        return res.getString(R.string.text_quest_type) + res.getString(stringId);
    }
}
