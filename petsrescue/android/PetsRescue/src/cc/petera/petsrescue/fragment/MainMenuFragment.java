package cc.petera.petsrescue.fragment;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.ListFragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;

public class MainMenuFragment extends ListFragment {
    static class MainMenuItem {
        int mTextId;
        int mIconId;
        public MainMenuItem(int textId, int iconId) {
            mTextId = textId;
            mIconId = iconId;
        }
        public int getTextId() {
            return mTextId;
        }
        public int getIconId() {
            return mIconId;
        }
    }

    class MainMenuListAdapter extends ArrayAdapter<MainMenuItem> {
        public MainMenuListAdapter(Context context, MainMenuItem[] objects) {
            super(context, 0, objects);
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (null == convertView) {
                convertView = mInflater.inflate(R.layout.item_main_menu, null);
            }

            MainMenuItem item = this.getItem(position);
            LinearLayout itemLayout = (LinearLayout) convertView;
            TextView textView = (TextView) itemLayout.findViewById(R.id.text_main_menu);
            textView.setText(item.getTextId());
            ImageView iconView = (ImageView) itemLayout.findViewById(R.id.image_main_menu);
            iconView.setImageResource(item.getIconId());

            return itemLayout;
        }
    }

    LayoutInflater mInflater;
    MainMenuItem[] mItems = new MainMenuItem[] {
        new MainMenuItem(R.string.menu_new_quest, R.drawable.ic_new_quest),
        new MainMenuItem(R.string.menu_quest_pager, R.drawable.ic_quest_list),
        new MainMenuItem(R.string.menu_animal_list, R.drawable.ic_animal_list),
    };

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mInflater = LayoutInflater.from(this.getActivity());
        this.setListAdapter(new MainMenuListAdapter(this.getActivity(), mItems));
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        MainActivity mainActivity = (MainActivity) this.getActivity();
        switch (position) {
        case 0:
            mainActivity.showNewMissionPage();
            break;
        case 1:
            mainActivity.showMissionPagerPage(MissionPagerFragment.TAB_ONGOING);
            break;
        case 2:
            mainActivity.showAnimalListPage();
            break;
        }
    }
}
