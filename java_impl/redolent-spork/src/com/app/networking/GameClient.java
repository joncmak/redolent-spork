package com.app.networking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;

import config.GamePropertiesReader;

public class GameClient
{
	private int mPlayerID;
	private Socket mSocket;
	
	private BufferedReader mInputStream;
	private PrintWriter mOutputStream;
	
	public GameClient(int pPlayerID, String pServerAddress)
	{
		mPlayerID = pPlayerID;
		
		GamePropertiesReader propReader = new GamePropertiesReader();
		List<String> properties = propReader.getProperties();
		
		int port = Integer.parseInt(properties.get(1));
		try 
		{
			mSocket = new Socket(pServerAddress, port);
			mInputStream = new BufferedReader(new InputStreamReader(mSocket.getInputStream()));
			mOutputStream = new PrintWriter(mSocket.getOutputStream(), true);
		} 
		catch (UnknownHostException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		catch (IOException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public int getID()
	{
		return mPlayerID;
	}
	
	public void play()
	{
		String response;
		
		//gameplay code here
	}
}
