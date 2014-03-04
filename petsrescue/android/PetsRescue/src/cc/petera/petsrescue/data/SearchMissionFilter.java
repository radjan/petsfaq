package cc.petera.petsrescue.data;

public class SearchMissionFilter {
    public boolean checkHostId = true;
    public long host_id;
    public boolean checkCompleted = true;
    public boolean completed;

    public boolean filter(Mission mission) {
        if (checkHostId && this.host_id != mission.host_id) {
            return false;
        }
        else if (checkCompleted && this.completed != mission.completed) {
            return false;
        }

        return true;
    }
}
