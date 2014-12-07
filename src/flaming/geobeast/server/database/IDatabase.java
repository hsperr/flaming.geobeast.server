package flaming.geobeast.server.database;

public interface IDatabase {
	void insert(String userID, String data);
	String retrieveUser(String userID);
}
