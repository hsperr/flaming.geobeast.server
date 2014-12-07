package flaming.geobeast.server.handlers;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;
import java.util.HashMap;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import flaming.geobeast.server.database.IDatabase;


public class ReceiveUserData extends AbstractHandler {
	
	private IDatabase database = null;
	
	public ReceiveUserData(IDatabase db) {
		this.database = db;
	}

	@Override
	public void handle(String target, Request baseRequest, HttpServletRequest request,
			HttpServletResponse response) throws IOException, ServletException {
		response.setContentType("text/html; charset=utf-8");
		response.setStatus(HttpServletResponse.SC_OK);
		
		//PrintWriter out = response.getWriter();
		String userID = request.getParameter("userID");
		String userLocation = request.getParameter("location");
		
		System.out.println(request.getRemoteAddr());
		System.out.println(request.getRemoteHost());
		System.out.println(request.getRemoteUser());
		
		System.out.println(request.getParameter("userID"));
		System.out.println(request.getParameter("location"));

		System.out.println(request.getQueryString());
		PrintWriter writer = response.getWriter();
		writer.println("<h1>Hello "+request.getParameter("userID")+"</h1><br>");
		writer.println("Current Position:"+userLocation+"<br>");			
	
		try {
			writer.println("Last Position: "+this.database.retrieveUser(userID));			
		} catch (Exception e) {
			writer.println("You have not been here, haven't you?");
		}
		
		
		this.database.insert(userID, userLocation);
		
		baseRequest.setHandled(true);
		
	}

}
