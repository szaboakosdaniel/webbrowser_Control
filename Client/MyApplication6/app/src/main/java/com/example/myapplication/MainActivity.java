package com.example.myapplication;

/*
import androidx.appcompat.app.AppCompatActivity;
import java.net.*; //TCP-IP socket communication
import java.io.*;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        String serverIP ="192.168,1,5";
        int serverPort =12345;
        try {
            Socket socket = new Socket(serverIP, serverPort);

            OutputStreamWriter out = new OutputStreamWriter(socket.getOutputStream());
            BufferedWriter writer = new BufferedWriter(out);
            String message = "hello";
            writer.write(message);
            writer.newLine();
            writer.flush();
            //System.out.println("Üzenet elküldve: " + message);

            writer.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        //setContentView(R.layout.activity_main);
    }
}
*/
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import android.widget.Button;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    private volatile boolean isRunning = false;
    String serverIP = "192.168.1.103"; // Pontokkal elválasztva
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
        // Hálózati műveleteket nem végezhetünk a fő szálon

          networkThread = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    socket = new Socket(serverIP, serverPort);
                    out = new OutputStreamWriter(socket.getOutputStream());
                    writer = new BufferedWriter(out);
                   // message = "hello";
                    // writer.write(message);
                    //writer.newLine();
                   // writer.flush();
                   // writer.close();
                    //out.close();
                    //socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
        });
        networkThread.start();




        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                messageThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            // socket = new Socket(serverIP, serverPort);
                            //out = new OutputStreamWriter(socket.getOutputStream());
                            // BufferedWriter writer = new BufferedWriter(out);
                            message = "hello";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            //writer.close();
                            //out.close();
                            //socket.close();
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
                            // socket = new Socket(serverIP, serverPort);
                            //out = new OutputStreamWriter(socket.getOutputStream());
                            // BufferedWriter writer = new BufferedWriter(out);
                            message = "korte";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            //writer.close();
                            //out.close();
                            //socket.close();
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
                            // socket = new Socket(serverIP, serverPort);
                            //out = new OutputStreamWriter(socket.getOutputStream());
                            // BufferedWriter writer = new BufferedWriter(out);
                            message = "alma";
                            writer.write(message);
                            writer.newLine();
                            writer.flush();
                            //writer.close();
                            //out.close();
                            //socket.close();
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
