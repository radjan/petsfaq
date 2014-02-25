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
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.data.SearchFilter;
import cc.petera.petsrescue.provider.ContextProvider;
import cc.petera.petsrescue.provider.MissionProvider;

public class MissionListFragment extends ListFragment {

    class QuestListAdapter extends BaseAdapter {
        @Override
        public int getCount() {
            return mMissions.size();
        }
        @Override
        public Object getItem(int position) {
            return mMissions.get(position);
        }
        @Override
        public long getItemId(int position) {
            return position;
        }
        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (null == convertView) {
                convertView = mInflater.inflate(R.layout.item_mission, null);
            }

            Mission mission = (Mission) getItem(position);

            LinearLayout itemLayout = (LinearLayout) convertView;
            TextView nameView = (TextView) itemLayout.findViewById(R.id.text_name);
            TextView typeView = (TextView) itemLayout.findViewById(R.id.text_type);
            nameView.setText(mission.animal.name);
            typeView.setText(getQuestTypeLabel(mission.type));

            return itemLayout;
        }
    }

    Handler mHandler = new Handler();
    LayoutInflater mInflater;
    QuestListAdapter mAdapter = new QuestListAdapter();
    SearchFilter mSearchFilter;
    ArrayList<Mission> mMissions = new ArrayList<Mission>();

    ContextProvider mContextProvider = new ContextProvider() {
        @Override
        public Handler getHandler() {
            return mHandler;
        }
        @Override
        public Context getContext() {
            return getActivity();
        }
        @Override
        public String getToken() {
            return ((MainActivity) getActivity()).getToken();
        }
    };

    MissionProvider.SearchMissionListener mSearchMissionCompleteListener = new MissionProvider.SearchMissionListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished(ArrayList<Mission> results) {
            mMissions = results;
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
        Mission mission = (Mission) this.getListAdapter().getItem(position);
        mainActivity.showMissionDetailPage(mission);
    }

    public void setSearchFilter(SearchFilter searchFilter) {
        mSearchFilter = searchFilter;
        refresh();
    }

    public void refresh() {
        if (null == mSearchFilter || null == getActivity()) {
            return;
        }
        ((MainActivity) this.getActivity()).getMissionProvider().searchMission(mSearchFilter, mSearchMissionCompleteListener);
    }

    String getQuestTypeLabel(int type) {
        Resources res = this.getActivity().getResources();
        int stringId = 0;
        switch (type) {
        case Mission.TYPE_RESCUE:
           stringId = R.string.quest_type_rescue;
           break;
        case Mission.TYPE_PICKUP:
            stringId = R.string.quest_type_pickup;
            break;
        case Mission.TYPE_STAY:
            stringId = R.string.quest_type_stay;
            break;
        case Mission.TYPE_DELIVER:
            stringId = R.string.quest_type_deliver;
            break;
        case Mission.TYPE_ADOPT:
            stringId = R.string.quest_type_adopt;
            break;
        }
        return res.getString(R.string.text_quest_type) + res.getString(stringId);
    }
}
