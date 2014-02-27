package cc.petera.petsrescue.data;

import java.util.Date;

import org.json.JSONException;
import org.json.JSONObject;

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
    public String status;
    public String name;
    public Date createddatetime;
    public boolean completed;
    public String note;
    public Date due_time;
    public long dest_location_id = MissionProvider.INVALID_ID;
    public long from_location_id = MissionProvider.INVALID_ID;
    public String place;
    public Animal animal;
    public long host_id = MissionProvider.INVALID_ID;
    public Date updateddatetime;
    public int type = TYPE_COUNT;
    public String requirement;
    public String period;
    public String skill;

    public static String getTypeName(int type) {
        if (type < 0 || type >= TYPE_COUNT) {
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
        return TYPE_COUNT;
    }

    static Date parseDate(String dateStr) {
        //TODO:
        return null;
    }

    public static Mission fromJSON(JSONObject obj) {
        Mission mission = new Mission();
        mission.animal = new Animal();

        try {
            //TODO: other fields
            mission.id = obj.getLong("id");
            mission.status = obj.getString("status");
            mission.name = obj.getString("name");
            mission.createddatetime = parseDate(obj.getString("createddatetime"));
            mission.completed = obj.getBoolean("completed");
            mission.note = obj.getString("note");
            mission.due_time = parseDate(obj.getString("due_time"));
            mission.place = obj.getString("place");
            mission.animal.id = obj.getLong("animal_id");
            mission.host_id = obj.getLong("host_id");
            mission.updateddatetime = parseDate(obj.getString("updateddatetime"));
            mission.type = getType(obj.getString("type"));
        }
        catch (JSONException e) {
        }

        return mission;
    }
}
