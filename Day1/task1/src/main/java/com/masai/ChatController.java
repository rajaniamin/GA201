package com.masai;

import org.apache.http.HttpEntity;
import org.apache.http.HttpHeaders;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
@RequestMapping("/chat")
public class ChatController {

    @Value("${openai.apiKey}")
    private String apiKey;

    @PostMapping(consumes = MediaType.TEXT_PLAIN_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String chat(@RequestBody String userInput) throws IOException {
        String openAiUrl = "https://api.openai.com/v1/engines/davinci-codex/completions";
        String openAiPrompt = "User: " + userInput + "\nAI:";

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(openAiUrl);

        httpPost.setHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        httpPost.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey);

        String requestBody = "{\"prompt\": \"" + openAiPrompt + "\", \"max_tokens\": 100}";
        HttpEntity requestEntity = new StringEntity(requestBody);
        httpPost.setEntity(requestEntity);

        HttpResponse response = httpClient.execute(httpPost);
        BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));

        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }

        httpClient.close();

        return sb.toString();
    }
}
