package cc.petera.petsrescue.data;

import cc.petera.petsrescue.provider.MissionProvider;

public class Mission {
    private static final String[] sTypeNames = { "rescue", "pickup", "stay", "deliver", "adopt" };
    public static final int TYPE_RESCUE = 0;
    public static final int TYPE_PICKUP = 1;
    public static final int TYPE_STAY = 2;
    public static final int TYPE_DELIVER = 3;
    public static final int TYPE_ADOPT = 4;
    public static final int TYPE_COUNT = 5;

    //TODO: getter/setter?
    public long id = MissionProvider.INVALID_ID;
    public String name;
    public int type;
    public String place;
    public String note;
    public boolean completed;
    public long dest_location_id = MissionProvider.INVALID_ID;
    public long host_id = MissionProvider.INVALID_ID;
    public long from_location_id = MissionProvider.INVALID_ID;
    public String requirement;
    public String period;
    public String skill;
    public Animal animal;

    public static String getTypeName(int type) {
        if (type < 0 || type >= TYPE_COUNT) {
            return "";
        }
        return sTypeNames[type];
    }
}
