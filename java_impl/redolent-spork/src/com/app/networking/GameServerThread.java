package com.app.networking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class GameServerThread
{
	private GameServerHandler mCurrentPlayer;
	private List<GameServerHandler> mPlayerList = new ArrayList<GameServerHandler>();
	private List<PrintWriter> mWriterList = new ArrayList<PrintWriter>();
	
	public void setCurrentPlayer(GameServerHandler pPlayer)
	{
		mCurrentPlayer = pPlayer;
	}
	
	public GameServerHandler getCurrentPlayer()
	{
		return mCurrentPlayer;
	}
	
	public void addPlayer(GameServerHandler pPlayer)
	{
		mPlayerList.add(pPlayer);
	}
	
	public GameServerHandler getPlayer(int pPlayerID)
	{
		return mPlayerList.get(pPlayerID);
	}
	
	public synchronized boolean legalMove(GameServerHandler pPlayer)
	{
		if(pPlayer == mCurrentPlayer)
		{
			int playerID = pPlayer.getID();
			
			int nextPlayerID = playerID == mPlayerList.size() ? 0 : playerID+1;
			mCurrentPlayer = getPlayer(nextPlayerID);
			return true;
		}
		return false;
	}
	
	/**
	 * 
	 *
	 */
	public class GameServerHandler extends Thread
	{
		private int mPlayerID;
		
		private Socket mSocket;
		private BufferedReader mInput;
		private PrintWriter mOutput;
		
		public GameServerHandler(Socket pSocket, int pPlayerID)
		{
			System.out.println("New Connection: Player " + pPlayerID + " has connected.");
			mSocket = pSocket;
			mPlayerID = pPlayerID;
			
			try
			{
				mInput = new BufferedReader(new InputStreamReader(mSocket.getInputStream()));
				mOutput = new PrintWriter(mSocket.getOutputStream(), true);
			} 
			catch (IOException e)
			{
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			mWriterList.add(mOutput);
			mOutput.println("MESSAGE Waiting for other players to connect");
		}
		
		public int getID()
		{
			return mPlayerID;
		}
		
		public void run()
		{
			try
			{
				mOutput.println("MESSAGE All players connected");
				
				while(true)
				{
					String command = mInput.readLine();
					System.out.println(command);
					//parseCommand
					
					if(legalMove(this))
					{
						mOutput.println("VALID");
					}
				}
			} catch (IOException e)
			{
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			finally
			{
				try
				{
					mSocket.close();
				} catch (IOException e)
				{
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
	}
}

