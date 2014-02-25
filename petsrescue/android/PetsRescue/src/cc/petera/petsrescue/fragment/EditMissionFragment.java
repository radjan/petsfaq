package cc.petera.petsrescue.fragment;

import java.io.InputStream;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ScrollView;
import android.widget.Spinner;
import android.widget.SpinnerAdapter;
import cc.petera.petsrescue.MainActivity;
import cc.petera.petsrescue.R;
import cc.petera.petsrescue.data.Animal;
import cc.petera.petsrescue.data.Mission;

public class EditMissionFragment extends Fragment {
    private static final String TAG = "EditMissionFragment";

    public interface Listener {
        void onCancel(EditMissionFragment fragment);
        void onOK(EditMissionFragment fragment, Mission mission);
    }

    Listener mListener;
    Bitmap mPhoto;
    Mission mMission;

    EditText mNameEdit;
    Spinner mTypeSpinner;
    Spinner mSubtypeSpinner;
    EditText mPlaceEdit;
    Spinner mHealthSpinner;
    CheckBox mCaughtCheck;
    ImageView mPhotoView;
    EditText mNoteEdit;
    Button mCancelButton;
    Button mOkButton;

    MainActivity.ActivityResultListener mPickPhotoListener = new MainActivity.ActivityResultListener() {
        @Override
        public void onActivityResult(int resultCode, Intent returnedIntent) {
            if (Activity.RESULT_OK != resultCode) {
                return;
            }
            Uri uri = returnedIntent.getData();
            mPhoto = null;
            try {
                InputStream is = getActivity().getContentResolver().openInputStream(uri);
                mPhoto = BitmapFactory.decodeStream(is);
            }
            catch (Exception e) {
                Log.d(TAG, "Failed to open " + uri);
            }
            mPhotoView.setImageBitmap(mPhoto);
        }
    };

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ScrollView scrollView = (ScrollView) inflater.inflate(R.layout.fragment_edit_mission, container, false);
        mNameEdit = (EditText) scrollView.findViewById(R.id.edit_pet_name);
        mTypeSpinner = (Spinner) scrollView.findViewById(R.id.spinner_pet_type);
        mSubtypeSpinner = (Spinner) scrollView.findViewById(R.id.spinner_pet_subtype);
        mPlaceEdit = (EditText) scrollView.findViewById(R.id.edit_quest_place);
        mHealthSpinner = (Spinner) scrollView.findViewById(R.id.spinner_pet_health);
        mCaughtCheck = (CheckBox) scrollView.findViewById(R.id.check_pet_caught);
        mPhotoView = (ImageView) scrollView.findViewById(R.id.image_pet_photo);
        mNoteEdit = (EditText) scrollView.findViewById(R.id.edit_quest_note);
        mCancelButton = (Button) scrollView.findViewById(R.id.button_cancel);
        mOkButton = (Button) scrollView.findViewById(R.id.button_ok);

        mNameEdit.addTextChangedListener(new TextWatcher() {
            @Override
            public void afterTextChanged(Editable s) {
            }
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                updateOkButton();
            }
        });

        mTypeSpinner.setAdapter(ArrayAdapter.createFromResource(getActivity(), R.array.pet_type, android.R.layout.simple_spinner_item));
        mTypeSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
                int subtypeArrayId = ((MainActivity) getActivity()).getPetSubtypeArrayId(pos);
                if (0 == subtypeArrayId) {
                    return;
                }
                SpinnerAdapter adapter = ArrayAdapter.createFromResource(getActivity(), subtypeArrayId, android.R.layout.simple_spinner_item);
                mSubtypeSpinner.setAdapter(adapter);
            }
            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                mSubtypeSpinner.setAdapter(null);
            }
        });

        mPlaceEdit.addTextChangedListener(new TextWatcher() {
            @Override
            public void afterTextChanged(Editable s) {
            }
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                updateOkButton();
            }
        });

        mHealthSpinner.setAdapter(ArrayAdapter.createFromResource(getActivity(), R.array.pet_health, android.R.layout.simple_spinner_item));

        mPhotoView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ((MainActivity) getActivity()).pickPhoto(mPickPhotoListener);
            }
        });

        mCancelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clear();
                hideKeyboard();
                mListener.onCancel(EditMissionFragment.this);
            }
        });
        mOkButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Mission mission = getMission();
                clear();
                hideKeyboard();
                mListener.onOK(EditMissionFragment.this, mission);
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
    }

    void clear() {
        mPhoto = null;
    }

    public void updateViews() {
        if (null == mMission) {
            mNameEdit.setText("");
            mTypeSpinner.setSelection(0);
            mHealthSpinner.setSelection(0);
            mPlaceEdit.setText("");
            mCaughtCheck.setVisibility(View.VISIBLE);
            mCaughtCheck.setChecked(false);
            mPhotoView.setImageBitmap(null);
            mNoteEdit.setText("");
            mOkButton.setText(R.string.button_new_quest);
        }
        else {
            mNameEdit.setText(mMission.animal.name);
            mTypeSpinner.setSelection(mMission.animal.type);
            mHealthSpinner.setSelection(mMission.animal.subtype);
            mPlaceEdit.setText(mMission.place);
            mCaughtCheck.setVisibility(View.GONE);
            mPhotoView.setImageBitmap(mMission.animal.photo);
            mNoteEdit.setText(mMission.note);
            mOkButton.setText(R.string.button_ok);
        }

        updateOkButton();
    }

    Mission getMission() {
        Mission mission = new Mission();
        mission.animal = new Animal();
        if (null == mMission) {
            mission.type = mCaughtCheck.isChecked() ? Mission.TYPE_STAY : Mission.TYPE_RESCUE;
            mission.completed = false;
        }
        else {
            mission.id = mMission.id;
            mission.type = mMission.type;
            mission.completed = mMission.completed;
            mission.animal.id = mMission.animal.id;
        }
        mission.animal.name = mNameEdit.getText().toString();
        mission.animal.type = (int) mTypeSpinner.getSelectedItemId();
        mission.animal.subtype = (int) mSubtypeSpinner.getSelectedItemId();
        mission.animal.health = (int) mHealthSpinner.getSelectedItemId();
        mission.animal.photo = mPhoto;
        mission.place = mPlaceEdit.getText().toString();
        mission.note = mNoteEdit.getText().toString();

        return mission;
    }

    void updateOkButton() {
        if (0 == mNameEdit.length()) {
            mOkButton.setEnabled(false);
            return;
        }
        else if (0 == mPlaceEdit.length()) {
            mOkButton.setEnabled(false);
            return;
        }

        mOkButton.setEnabled(true);
    }

    void hideKeyboard() {
        InputMethodManager imm = (InputMethodManager) getActivity().getSystemService(Context.INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(this.getActivity().getCurrentFocus().getWindowToken(), 0);
    }
}
