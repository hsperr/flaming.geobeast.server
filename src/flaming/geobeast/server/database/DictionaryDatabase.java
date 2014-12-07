package flaming.geobeast.server.database;
import java.util.HashMap;

public class DictionaryDatabase implements IDatabase{
	HashMap<String, String> data = new HashMap<String, String>();

	public DictionaryDatabase() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public void insert(String userID, String data) {
		this.data.put(userID, data);
	}

	@Override
	public String retrieveUser(String userID) {
		return this.data.get(userID);
	}
	
}