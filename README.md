# Enable your youtube data API

### follow the link below and check out step 3.
https://developers.google.com/youtube/v3/getting-started?hl=zh-tw

### Ref
https://martinfowler.com/articles/refactoring-external-service.html

# Purpose
1. Read youtube videos list from videos.json.
2. Retrive the video details through youtube data API by ID.
The youtube resopnse would be
```json
{
  "kind": "youtube#videoListResponse",
  "etag": "iLNKj1SXASDkYAfzQSn9fR_lsx8",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "_UzZU4qdLl5BSbgRGv40Y7XT7-E",
      "id": "9hyV27g9YFk",
      "snippet": {
        "publishedAt": "2020-05-12T10:01:00Z",
        "channelId": "UCg0m_Ah8P_MQbnn77-vYnYw",
        ...
      },
      "contentDetails": {
        ...
      },
      "statistics": {
        "viewCount": "191120",
        ...
      }
    },
    {
      "kind": "youtube#video",
      "etag": "C0GkMuEsoRt9z4rgDb4-MR31-Wk",
      "id": "C2WCbHTTB-4",
      "snippet": {
        "publishedAt": "2018-11-17T09:23:21Z",
        "channelId": "UCUMzET2JdWLxZGhvTKCIK-A",
        ...
      },
      "contentDetails": {
        ...
      },
      "statistics": {
        "viewCount": "3767755",
        ...
      }
    },
    {
      "kind": "youtube#video",
      "etag": "YbDHEhTObuzXkyvmMIDZDxXJbpo",
      "id": "l-pWz9p7AvU",
      "snippet": {
        "publishedAt": "2020-05-09T03:39:11Z",
        "channelId": "UCjEGRKDfUOel8Hp9Iumw5NQ",
        ...
      },
      "contentDetails": {
        ...
      },
      "statistics": {
        "viewCount": "235127",
        ...
      }
    }
  ],
  "pageInfo": {
    "totalResults": 3,
    "resultsPerPage": 3
  }
}
```
3. Enrich the video in videos list, such as "views" and "monthlyViews".
The output json would be
```json
[
  {
    "youtubeID": "9hyV27g9YFk",
    "views": 191153,
    "monthlyViews": 5814237.083333333
  },
  {
    "youtubeID": "C2WCbHTTB-4",
    "views": 3767758,
    "monthlyViews": 211054.58410067527
  },
  {
    "youtubeID": "l-pWz9p7AvU",
    "views": 235130,
    "monthlyViews": 1787967.7083333333
  }
]
```

#
![](https://martinfowler.com/articles/refactoring-external-service/no-sep.png)
![](https://martinfowler.com/articles/refactoring-external-service/sep-connection.png)
![](https://martinfowler.com/articles/refactoring-external-service/gateway-sketch.png)
![](https://martinfowler.com/articles/refactoring-external-service/sep-gateway.png)
