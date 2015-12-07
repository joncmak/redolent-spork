package config;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class GamePropertiesReader
{
	public GamePropertiesReader()
	{
	}
	
	public List<String> getProperties()
	{
		List<String> result = new ArrayList<String>();
		
		Properties properties = new Properties();
		String filename = "server.properties";
		
		InputStream inputStream = getClass().getClassLoader().getResourceAsStream(filename);
		try
		{
			properties.load(inputStream);
		} catch (IOException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		result.add(properties.getProperty("server_ip"));
		result.add(properties.getProperty("server_port"));
		
		return result;
	}
}
