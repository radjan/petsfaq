package cc.petera.petsrescue.data;

import android.graphics.Bitmap;
import cc.petera.petsrescue.provider.MissionProvider;

public class Animal {
    public static final int TYPE_CAT = 0;
    public static final int TYPE_DOG = 1;
    public static final int SUBTYPE_CAT_ADULT = 0;
    public static final int SUBTYPE_CAT_KITTEN = 1;
    public static final int SUBTYPE_DOG_BIG = 0;
    public static final int SUBTYPE_DOG_SMALL = 1;

    static final String[] sTypeNames = { "cat", "dog" };
    static final String[] sSubtypeCatNames = { "adult", "kitten" };
    static final String[] sSubtypeDogNames = { "big", "small" };

    //TODO: getter/setter?
    public long id = MissionProvider.INVALID_ID;
    public String name;
    public int type;
    public int subtype;
    public String description;
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
}
