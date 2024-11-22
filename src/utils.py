import requests


def fetch_yt_data(video_id: str):
    headers = {
        "origin": "https://www.youtube.com",
        "referer": "https://www.youtube.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    }

    params = {
        "key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
    }

    json_data = {
        "context": {
            "client": {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231101.05.00",
            },
        },
        "videoId": video_id,
    }

    response = requests.post(
        "https://www.youtube.com/youtubei/v1/player",
        params=params,
        headers=headers,
        json=json_data,
    )

    response_data = response.json()
    return response_data


def get_hls_manifest_url(video_id: str):
    yt_data = fetch_yt_data(video_id)
    return (
        yt_data["streamingData"]["hlsManifestUrl"]
        if "streamingData" in yt_data and "hlsManifestUrl" in yt_data["streamingData"]
        else None
    )
