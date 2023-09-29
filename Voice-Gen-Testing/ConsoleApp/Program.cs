
const string ApiUrl = "http://localhost:5001/text-to-speech";

string text = "> When I was 13 I got curious and started snooping my sister's room forunderwear and stuff.\r\n> she lived away at Uni and parents worked late 5o I had lots of time alone athome.\r\n> I had many faps with her underwear wrapped around my cock in her bed.\r\n> Eventually I started wearing them, and then soon after that bras too.\r\n> 1 got stupid and started wearing them around the house while I was alone.\r\n> Sis come home from uni a few days early to surprise parents for mumsBirthday\r\n> Catches me sitting on the sofa in her old thong and bra.\r\n> 1 run to my room\r\n> She eventually comes to talk to me.\r\n> tells me she isnt mad and its ok\r\n> I'm stil too embarrassed\r\n> next day she comes to my room with a bag and tells me she was having aclear out and thought I might like to try some of it\r\n> she leaves me alone again\r\n> 1look through and see a lacy red bra and pant set\r\n> try it on and immediately hard\r\n> she comes to my room and I dive under my covers\r\n> she asks if I'm wearing some now\r\n> um...yes\"\r\n> asks if she can see\r\n> reluctantly uncover myself\r\n> she lets out a litle gasp and then tells me that I look kinda sexy\r\n> she then looks down at my hard cock straining against the lace and says youclearly like that set\r\n> long story short we spent the next week hanging out and trying her iothes,she even took me shopping and we bought some matching sets.\r\n> started wearing them together and just chiling\r\n> day before she goes back to uni we are on my bed in matching panties setsand we start making out but she stops it and leaves\r\n> don't talk for a few days\r\n> eventually she messages and apologises and tells me she's sorry for whatshe did.\r\n> don't really talk much til she come shome for Xmas\r\n> she comes to my room and tells me she has a special present\r\n> tells me to open it then\r\n> open itand its a sexy litle lacy thong set\r\n> tells me I can put it on now if I like\r\n> get naked in front of her and I'm hard at already\r\n> putit on and she helps me with the bra";
text = text.Replace(">", String.Empty);

await TextToSpeechAsync(text);

async Task TextToSpeechAsync(string text)
{
    using HttpClient client = new HttpClient();
    using MultipartFormDataContent content = new MultipartFormDataContent
    {
        { new StringContent(text), "text" }
    };

    HttpResponseMessage response = await client.PostAsync(ApiUrl, content);

    if (response.IsSuccessStatusCode)
    {
        byte[] mp3Bytes = await response.Content.ReadAsByteArrayAsync();
        File.WriteAllBytes("output_other.mp3", mp3Bytes);
        Console.WriteLine("MP3 file saved as output.mp3");
    }
    else
    {
        string error = await response.Content.ReadAsStringAsync();
        Console.WriteLine($"Error: {error}");
    }
}
