package flaming.geobeast.server.main;

import org.eclipse.jetty.server.Server;

import flaming.geobeast.server.database.DictionaryDatabase;
import flaming.geobeast.server.handlers.ReceiveUserData;

public class Webserver {

	public static void main(String[] args) {
		
		try {
			Server server = new Server(8080);
			server.setHandler(new ReceiveUserData(new DictionaryDatabase()));
			server.start();
			server.dumpStdErr();
			server.join();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
