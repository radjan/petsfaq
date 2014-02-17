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
import cc.petera.petsrescue.data.Quest;

public class QuestDetailFragment extends Fragment {

    public interface Listener {
        //TODO:
    }

    Listener mListener;
    Quest mQuest;

    Button mEditButton;
    TextView mNameView;
    TextView mTypeView;
    TextView mLocationView;
    TextView mHealthView;
    ImageView mPhotoView;
    TextView mNoteView;
    Button mStartButton;
    Button mCancelButton;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ScrollView scrollView = (ScrollView) inflater.inflate(R.layout.fragment_quest_detail, container, false);
        mEditButton = (Button) scrollView.findViewById(R.id.button_edit_quest);
        mNameView = (TextView) scrollView.findViewById(R.id.text_pet_name);
        mTypeView = (TextView) scrollView.findViewById(R.id.text_pet_type);
        mLocationView = (TextView) scrollView.findViewById(R.id.text_quest_location);
        mHealthView = (TextView) scrollView.findViewById(R.id.text_pet_health);
        mPhotoView = (ImageView) scrollView.findViewById(R.id.image_pet_photo);
        mNoteView = (TextView) scrollView.findViewById(R.id.text_quest_note);
        mStartButton = (Button) scrollView.findViewById(R.id.button_start_quest);
        mCancelButton = (Button) scrollView.findViewById(R.id.button_cancel_quest);

        mEditButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                editQuest();
            }
        });

        mStartButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startQuest();
            }
        });

        mCancelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cancelQuest();
            }
        });

        updateViews();

        return scrollView;
    }

    public void setListener(Listener listener) {
        mListener = listener;
    }

    public void setQuest(Quest quest) {
        mQuest = quest;
        updateViews();
    }

    void updateViews() {
        if (null == getActivity() || null == mNameView) {
            return;
        }
        MainActivity mainActivity = (MainActivity) getActivity();
        mNameView.setText(mQuest.pet.name);
        mTypeView.setText(mainActivity.getPetSubtypeString(mQuest.pet.type, mQuest.pet.subtype));
        mLocationView.setText(mQuest.location);
        mHealthView.setText(mainActivity.getPetHealthString(mQuest.pet.health));
        mPhotoView.setImageBitmap(mQuest.pet.photo);
        mNoteView.setText(mQuest.note);

        mStartButton.setVisibility(View.GONE);
        mCancelButton.setVisibility(View.GONE);
        long ownerId = ((MainActivity) getActivity()).getOwnerId();
        if (ownerId == mQuest.ownerId) {
            mCancelButton.setVisibility(View.VISIBLE);
        }
        else if (Quest.OWNER_ID_NONE == mQuest.ownerId) {
            mStartButton.setVisibility(View.VISIBLE);
        }
    }

    void editQuest() {
        ((MainActivity) getActivity()).showEditQuestPage(mQuest);
    }

    void startQuest() {
        //TODO: confirm dialog
        ((MainActivity) getActivity()).startQuest(mQuest);
    }

    void cancelQuest() {
        //TODO: confirm dialog
        ((MainActivity) getActivity()).cancelQuest(mQuest);
    }
}
