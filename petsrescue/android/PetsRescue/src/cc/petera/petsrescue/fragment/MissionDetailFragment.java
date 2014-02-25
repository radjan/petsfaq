package cc.petera.petsrescue.fragment;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ScrollView;
import android.widget.TextView;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;
import cc.petera.petsrescue.data.Mission;
import cc.petera.petsrescue.provider.MissionProvider;

public class MissionDetailFragment extends Fragment {

    public interface Listener {
        //TODO:
    }

    Listener mListener;
    Mission mMission;

    Button mEditButton;
    TextView mNameView;
    TextView mTypeView;
    TextView mPlaceView;
    TextView mHealthView;
    ImageView mPhotoView;
    TextView mNoteView;
    Button mStartButton;
    Button mCancelButton;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ScrollView scrollView = (ScrollView) inflater.inflate(R.layout.fragment_mission_detail, container, false);
        mEditButton = (Button) scrollView.findViewById(R.id.button_edit_quest);
        mNameView = (TextView) scrollView.findViewById(R.id.text_pet_name);
        mTypeView = (TextView) scrollView.findViewById(R.id.text_pet_type);
        mPlaceView = (TextView) scrollView.findViewById(R.id.text_quest_place);
        mHealthView = (TextView) scrollView.findViewById(R.id.text_pet_health);
        mPhotoView = (ImageView) scrollView.findViewById(R.id.image_pet_photo);
        mNoteView = (TextView) scrollView.findViewById(R.id.text_quest_note);
        mStartButton = (Button) scrollView.findViewById(R.id.button_start_quest);
        mCancelButton = (Button) scrollView.findViewById(R.id.button_cancel_quest);

        mEditButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                editMission();
            }
        });

        mStartButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startMission();
            }
        });

        mCancelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cancelMission();
            }
        });

        updateViews();

        return scrollView;
    }

    public void setListener(Listener listener) {
        mListener = listener;
    }

    public void setMission(Mission mission) {
        mMission = mission;
        updateViews();
    }

    void updateViews() {
        if (null == getActivity() || null == mNameView) {
            return;
        }
        MainActivity mainActivity = (MainActivity) getActivity();
        mNameView.setText(mMission.animal.name);
        mTypeView.setText(mainActivity.getPetSubtypeString(mMission.animal.type, mMission.animal.subtype));
        mPlaceView.setText(mMission.place);
        mHealthView.setText(mainActivity.getPetHealthString(mMission.animal.health));
        mPhotoView.setImageBitmap(mMission.animal.photo);
        mNoteView.setText(mMission.note);

        mStartButton.setVisibility(View.GONE);
        mCancelButton.setVisibility(View.GONE);
        long userId = ((MainActivity) getActivity()).getUserId();
        if (userId == mMission.host_id) {
            mCancelButton.setVisibility(View.VISIBLE);
        }
        else if (MissionProvider.INVALID_ID == mMission.host_id) {
            mStartButton.setVisibility(View.VISIBLE);
        }
    }

    void editMission() {
        ((MainActivity) getActivity()).showEditMissionPage(mMission);
    }

    void startMission() {
        //TODO: confirm dialog
        ((MainActivity) getActivity()).startMission(mMission);
    }

    void cancelMission() {
        //TODO: confirm dialog
        ((MainActivity) getActivity()).cancelMission(mMission);
    }
}
