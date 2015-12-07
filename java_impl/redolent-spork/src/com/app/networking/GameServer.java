package com.app.networking;

import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.util.List;

import config.GamePropertiesReader;

public class GameServer
{
	private int mMaxPlayers;
	
	public GameServer()
	{
		GamePropertiesReader propReader = new GamePropertiesReader();
		List<String> properties = propReader.getProperties();
		
		int port = Integer.parseInt(properties.get(1));
		
		mMaxPlayers = 3;
		
		try
		{
			ServerSocket listener = new ServerSocket(port);
			System.out.println("Server Started on " + InetAddress.getLocalHost().getHostAddress() + ":" + port);
			
			try
			{				
				while (true)
				{
					GameServerThread game = new GameServerThread();

					for(int playerCount = 0; playerCount < mMaxPlayers; playerCount ++)
					{
						GameServerThread.GameServerHandler player = game.new GameServerHandler(listener.accept(), playerCount);
						game.addPlayer(player);
						
						if(null == game.getCurrentPlayer())
						{
							game.setCurrentPlayer(game.getPlayer(0));
						}

						player.start();
					}
				}
			}
			finally
			{
				listener.close();
			}
		} catch (IOException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@SuppressWarnings("unused")
	public static void main(String[] args)
	{
		GameServer server = new GameServer();
	}
}
