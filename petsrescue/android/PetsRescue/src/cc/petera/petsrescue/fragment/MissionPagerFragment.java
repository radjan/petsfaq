package cc.petera.petsrescue.fragment;

import java.lang.reflect.Field;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;
import cc.petera.petsrescue.data.SearchFilter;
import cc.petera.petsrescue.provider.MissionProvider;

public class MissionPagerFragment extends Fragment {
    private static final String TAG = "MissionPagerFragment";

    public static final int TAB_ONGOING = 0;
    public static final int TAB_AVAILABLE = 1;
    public static final int TAB_TRACKED = 2;
    public static final int TAB_COMPLETED = 3;

    public static final int TAB_COUNT = 4;

    class RescueListPagerAdapter extends FragmentPagerAdapter {
        public RescueListPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int i) {
            return mFragments[i];
        }

        @Override
        public int getCount() {
            return mFragments.length;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            switch (position) {
            case TAB_ONGOING:
                return getActivity().getString(R.string.title_quest_ongoing);
            case TAB_AVAILABLE:
                return getActivity().getString(R.string.title_quest_available);
            case TAB_TRACKED:
                return getActivity().getString(R.string.title_quest_tracked);
            case TAB_COMPLETED:
                return getActivity().getString(R.string.title_quest_completed);
            }
            Log.d(TAG, "getPageTitle " + position + " is not supported");
            return "";
        }
    }

    ViewPager mViewPager;
    RescueListPagerAdapter mAdapter;
    int mDefaultTab = TAB_ONGOING;
    MissionListFragment[] mFragments;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        mViewPager = (ViewPager) inflater.inflate(R.layout.fragment_mission_list, container, false);

        createFragments();
        mAdapter = new RescueListPagerAdapter(this.getChildFragmentManager());
        mViewPager.setAdapter(mAdapter);
        refresh();

        return mViewPager;
    }

    @Override
    public void onStart() {
        super.onStart();
        mViewPager.setCurrentItem(mDefaultTab);
    }

    @Override
    public void onDetach() {
        super.onDetach();

        // workaround for the bug https://code.google.com/p/android/issues/detail?id=42601
        try {
            Field childFragmentManager = Fragment.class.getDeclaredField("mChildFragmentManager");
            childFragmentManager.setAccessible(true);
            childFragmentManager.set(this, null);

        } catch (NoSuchFieldException e) {
            throw new RuntimeException(e);
        } catch (IllegalAccessException e) {
            throw new RuntimeException(e);
        }
    }

    void createFragments() {
        if (null != mFragments) {
            return;
        }

        //TODO:

        mFragments = new MissionListFragment[TAB_COUNT];
        mFragments[TAB_ONGOING] = new MissionListFragment();
        SearchFilter filter = new SearchFilter();
        filter.host_id = ((MainActivity) this.getActivity()).getUserId();
        filter.completed = false;
        mFragments[TAB_ONGOING].setSearchFilter(filter);

        mFragments[TAB_AVAILABLE] = new MissionListFragment();
        filter = new SearchFilter();
        filter.host_id = MissionProvider.INVALID_ID;
        filter.completed = false;
        mFragments[TAB_AVAILABLE].setSearchFilter(filter);

        mFragments[TAB_TRACKED] = new MissionListFragment();

        mFragments[TAB_COMPLETED] = new MissionListFragment();
        filter = new SearchFilter();
        filter.host_id = ((MainActivity) getActivity()).getUserId();
        filter.completed = true;
        mFragments[TAB_COMPLETED].setSearchFilter(filter);
    }

    public void refresh() {
        if (null == mFragments) {
            return;
        }
        for (MissionListFragment fragment : mFragments) {
            fragment.refresh();
        }
    }

    public void setDefaultTab(int tab) {
        mDefaultTab = tab;
    }
}
