package cc.petera.petsrescue.provider;

import android.content.Context;
import android.os.Handler;

public interface ContextProvider {
    Context getContext();
    Handler getHandler();
    String getToken();
}
