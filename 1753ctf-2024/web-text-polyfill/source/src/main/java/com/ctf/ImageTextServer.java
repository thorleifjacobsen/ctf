package com.ctf;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.util.UUID;

@WebServlet("/")
@MultipartConfig
public class ImageTextServer extends HttpServlet {

    private static Logger logger;
    private static String flag;

    public ImageTextServer() {
        logger = LogManager.getLogger(ImageTextServer.class.getName());
        flag = System.getenv("flag");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        if (request.getRequestURI().equals("/")) {
            response.setContentType("text/html");
            File file = new File("index.html");
            response.setStatus(HttpServletResponse.SC_OK);
            Files.copy(file.toPath(), response.getOutputStream());
        } else if (request.getRequestURI().equals("/logo.png")) {
            response.setContentType("text/html");
            File file = new File("logo.png");
            response.setStatus(HttpServletResponse.SC_OK);
            Files.copy(file.toPath(), response.getOutputStream());
        } else {
            response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        }

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        if (request.getRequestURI().equals("/process")) {
            Part filePart = request.getPart("image");
            String text = request.getParameter("text");
            try (InputStream fileContent = filePart.getInputStream()) {
                String filename = "/tmp/" + UUID.randomUUID().toString() + ".jpg";

                FileOutputStream fos = new FileOutputStream(filename);
                byte[] buffer = new byte[1024];
                int length;
                while ((length = fileContent.read(buffer)) > 0) {
                    fos.write(buffer, 0, length);
                }
                fos.close();

                File file = new File(filename);

                BufferedImage image = ImageIO.read(file);
                if (image == null) {
                    throw new IOException("Failed to decode image.");
                }
                Graphics graphics = image.getGraphics();
                graphics.setFont(new Font("Arial", Font.BOLD, 30));
                graphics.setColor(Color.BLACK);
                graphics.drawString(text, 10, image.getHeight() - 10);
                graphics.dispose();

                response.setContentType("image/png");
                ImageIO.write(image, "PNG", response.getOutputStream());
            } catch (IOException e) {
                response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            } catch (Exception e) {
                logger.error("Error processing image with text: " + text);
                response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            }
        } else {
            response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        }
    }
}