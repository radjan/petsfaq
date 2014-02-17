package cc.petera.petsrescue.data;

public class SearchFilter {
    public boolean checkOwnerId = true;
    public long ownerId;
    public boolean checkFinished = true;
    public boolean finished;

    public boolean filter(Quest quest) {
        if (checkOwnerId && this.ownerId != quest.ownerId) {
            return false;
        }
        else if (checkFinished && this.finished != quest.finished) {
            return false;
        }

        return true;
    }
}
