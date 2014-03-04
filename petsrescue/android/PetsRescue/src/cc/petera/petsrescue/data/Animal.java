package cc.petera.petsrescue.data;

import java.util.Date;

import org.json.JSONException;
import org.json.JSONObject;

import android.graphics.Bitmap;
import cc.petera.petsrescue.provider.MissionProvider;
import cc.petera.petsrescue.util.DateParser;

public class Animal {
    public static final int TYPE_UNKNOWN = -1;
    public static final int TYPE_CAT = 0;
    public static final int TYPE_DOG = 1;
    public static final int SUBTYPE_UNKNOWN = -1;
    public static final int SUBTYPE_CAT_ADULT = 0;
    public static final int SUBTYPE_CAT_KITTEN = 1;
    public static final int SUBTYPE_DOG_BIG = 0;
    public static final int SUBTYPE_DOG_SMALL = 1;

    static final String[] sTypeNames = { "cat", "dog" };
    static final String[] sSubtypeCatNames = { "adult", "kitten" };
    static final String[] sSubtypeDogNames = { "big", "small" };

    //TODO: getter/setter?
    public String status;
    public String description;
    public Date createddatetime;
    public Date updateddatetime;
    public long id = MissionProvider.INVALID_ID;
    public String name;
    public int type;
    public int subtype;
    public long owner_id = MissionProvider.INVALID_ID;
    public int health;
    public Bitmap photo;
    public long find_location_id = MissionProvider.INVALID_ID;
    public long current_location_id = MissionProvider.INVALID_ID;

    public static String getTypeName(int type) {
        if (type < 0 || type >= sTypeNames.length) {
            return "";
        }
        return sTypeNames[type];
    }

    public static int getType(String name) {
        for (int i = 0; i < sTypeNames.length; i++) {
            if (sTypeNames[i].equals(name)) {
                return i;
            }
        }
        return TYPE_UNKNOWN;
    }

    public static String getSubtypeName(int type, int subtype) {
        String[] subtypeNames = null;

        switch (type) {
        case TYPE_CAT:
            subtypeNames = sSubtypeCatNames;
            break;
        case TYPE_DOG:
            subtypeNames = sSubtypeDogNames;
            break;
        default:
            return "";
        }

        if (subtype < 0 || subtype >= subtypeNames.length) {
            return "";
        }
        return subtypeNames[subtype];
    }

    public static int getSubtype(int type, String name) {
        String[] subtypeNames = null;

        switch (type) {
        case TYPE_CAT:
            subtypeNames = sSubtypeCatNames;
            break;
        case TYPE_DOG:
            subtypeNames = sSubtypeDogNames;
            break;
        default:
            return SUBTYPE_UNKNOWN;
        }

        for (int i = 0; i < subtypeNames.length; i++) {
            if (subtypeNames[i].equals(name)) {
                return i;
            }
        }
        return SUBTYPE_UNKNOWN;
    }

    public static Animal fromJSON(JSONObject obj) {
        Animal animal = new Animal();

        try {
            //TODO: other fields
            animal.status = obj.getString("status");
            animal.description = obj.getString("description");
            animal.createddatetime = DateParser.parse(obj.getString("createddatetime"));
            animal.id = obj.getLong("id");
            animal.updateddatetime = DateParser.parse(obj.getString("updateddatetime"));
            animal.type = getType(obj.getString("type"));
            animal.type = getSubtype(animal.type, obj.getString("sub_type"));
            animal.name = obj.getString("name");
        }
        catch (JSONException e) {
        }

        return animal;
    }
}
