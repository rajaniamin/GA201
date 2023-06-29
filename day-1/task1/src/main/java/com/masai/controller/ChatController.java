package com.masai.controller;

import okhttp3.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
public class ChatController {

    @Value("${openai.api.key}")
    private String apiKey;

    @PostMapping("/chat")
    public String chat(@RequestBody String userInput) throws IOException {
        OkHttpClient client = new OkHttpClient();

        MediaType mediaType = MediaType.parse("application/json");
        RequestBody requestBody = RequestBody.create(mediaType, "{\"prompt\": \"" + userInput + "\"}");
        Request request = new Request.Builder()
                .url("https://api.openai.com/v1/engines/davinci-codex/completions")
                .post(requestBody)
                .addHeader("Content-Type", "application/json")
                .addHeader("Authorization", "Bearer " + apiKey)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String responseBody = response.body().string();
                // Extract and process the generated response from the responseBody
                return responseBody;
            } else {
                // Handle unsuccessful API response
                throw new IOException("Request failed: " + response.code() + " - " + response.message());
            }
        }
    }
}
