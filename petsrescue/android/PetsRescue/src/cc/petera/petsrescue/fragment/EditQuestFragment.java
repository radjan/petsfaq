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
import cc.petera.petsrescue.data.Pet;
import cc.petera.petsrescue.data.Quest;

public class EditQuestFragment extends Fragment {
    private static final String TAG = "EditQuestFragment";

    public interface Listener {
        void onCancel(EditQuestFragment fragment);
        void onOK(EditQuestFragment fragment, Quest quest);
    }

    Listener mListener;
    Bitmap mPhoto;
    Quest mQuest;

    EditText mNameEdit;
    Spinner mTypeSpinner;
    Spinner mSubtypeSpinner;
    EditText mLocationEdit;
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
        ScrollView scrollView = (ScrollView) inflater.inflate(R.layout.fragment_edit_quest, container, false);
        mNameEdit = (EditText) scrollView.findViewById(R.id.edit_pet_name);
        mTypeSpinner = (Spinner) scrollView.findViewById(R.id.spinner_pet_type);
        mSubtypeSpinner = (Spinner) scrollView.findViewById(R.id.spinner_pet_subtype);
        mLocationEdit = (EditText) scrollView.findViewById(R.id.edit_quest_location);
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

        mLocationEdit.addTextChangedListener(new TextWatcher() {
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
                mListener.onCancel(EditQuestFragment.this);
            }
        });
        mOkButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Quest quest = getQuest();
                clear();
                hideKeyboard();
                mListener.onOK(EditQuestFragment.this, quest);
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
    }

    void clear() {
        mPhoto = null;
    }

    public void updateViews() {
        if (null == mQuest) {
            mNameEdit.setText("");
            mTypeSpinner.setSelection(0);
            mHealthSpinner.setSelection(0);
            mLocationEdit.setText("");
            mCaughtCheck.setVisibility(View.VISIBLE);
            mCaughtCheck.setChecked(false);
            mPhotoView.setImageBitmap(null);
            mNoteEdit.setText("");
            mOkButton.setText(R.string.button_new_quest);
        }
        else {
            mNameEdit.setText(mQuest.pet.name);
            mTypeSpinner.setSelection(mQuest.pet.type);
            mHealthSpinner.setSelection(mQuest.pet.subtype);
            mLocationEdit.setText(mQuest.location);
            mCaughtCheck.setVisibility(View.GONE);
            mPhotoView.setImageBitmap(mQuest.pet.photo);
            mNoteEdit.setText(mQuest.note);
            mOkButton.setText(R.string.button_ok);
        }

        updateOkButton();
    }

    Quest getQuest() {
        Quest quest = new Quest();
        quest.pet = new Pet();
        if (null == mQuest) {
            quest.id = Quest.ID_UNKNOWN;
            quest.type = mCaughtCheck.isChecked() ? Quest.Type.HALFWAY : Quest.Type.CATCH;
            quest.ownerId = Quest.OWNER_ID_NONE;
            quest.finished = false;
            quest.pet.id = Quest.ID_UNKNOWN;
        }
        else {
            quest.id = mQuest.id;
            quest.type = mQuest.type;
            quest.ownerId = mQuest.ownerId;
            quest.finished = mQuest.finished;
            quest.pet.id = mQuest.pet.id;
        }
        quest.pet.name = mNameEdit.getText().toString();
        quest.pet.type = (int) mTypeSpinner.getSelectedItemId();
        quest.pet.subtype = (int) mSubtypeSpinner.getSelectedItemId();
        quest.pet.health = (int) mHealthSpinner.getSelectedItemId();
        quest.pet.photo = mPhoto;
        quest.location = mLocationEdit.getText().toString();
        quest.note = mNoteEdit.getText().toString();

        return quest;
    }

    void updateOkButton() {
        if (0 == mNameEdit.length()) {
            mOkButton.setEnabled(false);
            return;
        }
        else if (0 == mLocationEdit.length()) {
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
