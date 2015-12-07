package com.app.networking;

public class GameClient
{
	private int mPlayerID;
	
	public GameClient(int pPlayerID)
	{
		mPlayerID = pPlayerID;
	}
	
	public int getID()
	{
		return mPlayerID;
	}
}
