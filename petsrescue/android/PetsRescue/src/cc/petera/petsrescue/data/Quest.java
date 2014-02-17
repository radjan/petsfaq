package cc.petera.petsrescue.data;

public class Quest {
    public static final long ID_UNKNOWN = -1;
    public static final long OWNER_ID_NONE = -1;

    public enum Type {
        CATCH,
        TRANSPORT,
        HALFWAY,
        ADOPT,
        DONATE,
    }

    //TODO: getter/setter?
    public long id;
    public long ownerId;
    public boolean finished;
    public Type type;
    public Pet pet;
    public String location;
    public String note;
}
