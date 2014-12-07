package flaming.geobeast.server.main;

import org.eclipse.jetty.server.Server;

public class Webserver {

	public static void main(String[] args) {
		Server server = new Server(8080);
		
		try {
			server.start();
			server.dumpStdErr();
			server.join();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
