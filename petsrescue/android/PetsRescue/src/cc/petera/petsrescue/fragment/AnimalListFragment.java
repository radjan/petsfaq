package cc.petera.petsrescue.fragment;

import java.util.ArrayList;

import android.content.Context;
import android.content.res.Resources;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.ListFragment;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.TextView;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;
import cc.petera.petsrescue.data.Animal;
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.data.SearchAnimalFilter;
import cc.petera.petsrescue.provider.ContextProvider;
import cc.petera.petsrescue.provider.MissionProvider;

public class AnimalListFragment extends ListFragment {

    class AnimalListAdapter extends BaseAdapter {
        @Override
        public int getCount() {
            return mAnimals.size();
        }
        @Override
        public Object getItem(int position) {
            return mAnimals.get(position);
        }
        @Override
        public long getItemId(int position) {
            return position;
        }
        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (null == convertView) {
                convertView = mInflater.inflate(R.layout.item_animal, null);
            }

            Animal animal = (Animal) getItem(position);

            LinearLayout itemLayout = (LinearLayout) convertView;
            TextView nameView = (TextView) itemLayout.findViewById(R.id.text_name);
            TextView typeView = (TextView) itemLayout.findViewById(R.id.text_type);
            nameView.setText(animal.name);
            typeView.setText(getAnimalTypeLabel(animal.type, animal.subtype));

            return itemLayout;
        }
    }

    Handler mHandler = new Handler();
    LayoutInflater mInflater;
    AnimalListAdapter mAdapter = new AnimalListAdapter();
    SearchAnimalFilter mSearchFilter;
    ArrayList<Animal> mAnimals = new ArrayList<Animal>();

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

    MissionProvider.SearchAnimalListener mSearchAnimalCompleteListener = new MissionProvider.SearchAnimalListener() {
        @Override
        public ContextProvider getContextProvider() {
            return mContextProvider;
        }
        @Override
        public void onFinished(ArrayList<Animal> results) {
            mAnimals = results;
            mAdapter.notifyDataSetChanged();
        }
    };

    @Override
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        this.setEmptyText(getActivity().getString(R.string.animal_list_empty));
        this.getView().setBackgroundColor(0xFFFFFFFF);
        this.setHasOptionsMenu(true);
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mInflater = LayoutInflater.from(this.getActivity());
        this.setListAdapter(mAdapter);
        refresh();
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        inflater.inflate(R.menu.animal_list, menu);
        SearchView searchView = (SearchView) menu.findItem(R.id.action_search).getActionView();
        searchView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextChange(String s) {
                return false;
            }
            @Override
            public boolean onQueryTextSubmit(String s) {
                //TODO:
                return false;
            }
        });
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        MainActivity mainActivity = (MainActivity) this.getActivity();
        Animal animal = (Animal) this.getListAdapter().getItem(position);
        mainActivity.showAnimalDetailPage(animal);
    }

    public void refresh() {
        if (null == getActivity()) {
            return;
        }
        ((MainActivity) this.getActivity()).getMissionProvider().searchAnimal(mSearchFilter, mSearchAnimalCompleteListener);
    }

    String getAnimalTypeLabel(int type, int subtype) {
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
        default:
            stringId = R.string.quest_type_unknown;
            break;
        }
        return res.getString(R.string.text_quest_type) + res.getString(stringId);
    }
}
