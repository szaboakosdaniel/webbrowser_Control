package com.example.myapplication;


import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import java.net.*;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

import android.widget.Button;
import android.widget.EditText;
import android.view.View;
import java.util.Enumeration;
import android.util.Log;
public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    private volatile boolean isRunning = false;
    //String serverIP = "192.168.1.5"; // Pontokkal elválasztva
    int serverPort = 12345;
    Socket socket;
    OutputStreamWriter out;
    BufferedWriter writer;
    String message;
    Thread networkThread,messageThread;
    public void thread_interrupt() {
        messageThread.interrupt();
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button= (Button) findViewById(R.id.button);
        Button button2= (Button) findViewById(R.id.button2);
        Button button3= (Button) findViewById(R.id.button3);
        Button button4= (Button) findViewById(R.id.button4);
        Button button5= (Button) findViewById(R.id.button5);
        EditText url =(EditText) findViewById(R.id.url);


        // Example log messages
        Log.d(TAG, "Debug message");
        Log.e(TAG, "Error message");
        Log.i(TAG, "Info message");
        Log.v(TAG, "Verbose message");
        Log.w(TAG, "Warning message");
        // Hálózati műveleteket nem végezhetünk a fő szálon


          networkThread = new Thread(new Runnable() {
            @Override
            public void run() {
                ///////////////////
                String myIP=null;
                try {
                    Enumeration<NetworkInterface> networkInterfaces = NetworkInterface.getNetworkInterfaces();
                    while (networkInterfaces.hasMoreElements()) {
                        NetworkInterface networkInterface = networkInterfaces.nextElement();
                        Enumeration<InetAddress> inetAddresses = networkInterface.getInetAddresses();
                        while (inetAddresses.hasMoreElements()) {
                            InetAddress inetAddress = inetAddresses.nextElement();
                            if (!inetAddress.isLoopbackAddress() && !inetAddress.isLinkLocalAddress()) {
                               // System.out.println("Device IP Address: " + inetAddress.getHostAddress());
                                if(inetAddress instanceof Inet4Address) {
                                    myIP = inetAddress.getHostAddress();
                                    Log.i("KAP", myIP);
                                    System.out.println(myIP);
                                }
                            }
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }


                String subnet = null;
                String[] octets = myIP.split("\\.");

                // Ensure that there are at least 3 octets before removing the last one
                if (octets.length >= 3) {
                    // Remove the last octet
                     subnet = String.join(".", octets[0], octets[1], octets[2]);
                    System.out.println("Modified IP Address: " + subnet);
                } else {
                    System.out.println("Invalid IP Address");
                }

                Log.d("GAT",subnet);

                int i = 1;

                // Define the port to check (e.g., port 80 for HTTP)
                do{
                    String ipAddress = subnet + "." + i;
                    try {
                        socket = new Socket();
                        socket.connect(new InetSocketAddress(ipAddress, serverPort), 1000); // 1000 ms timeout
                        Log.v("NA","Found open port " + serverPort + " on host " + ipAddress);
                        out = new OutputStreamWriter(socket.getOutputStream());
                        writer = new BufferedWriter(out);
                        break;
                    } catch (Exception e) {
                        Log.v("NO","Can't connect open port " + serverPort + " on host " + ipAddress);
                        try {
                            socket.close();
                        } catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }
                    }
                    i++;
                }while(!socket.isConnected());


            }
        });
        networkThread.start();




        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            message = "open"+"đ"+url.getText().toString();
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            messageThread.interrupt();

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                });

                messageThread.start();
            }
        });


        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            message = "play_stop";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            messageThread.interrupt();

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                });

                messageThread.start();
            }
        });

        button3.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            message = "next";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            messageThread.interrupt();

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                });

                messageThread.start();
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            message = "accept_all";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            messageThread.interrupt();

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                });

                messageThread.start();
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            message = "full";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            messageThread.interrupt();

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                });

                messageThread.start();
            }
        });

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        try {
            writer.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
