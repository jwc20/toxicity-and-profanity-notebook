import ipfshttpclient

list_of_files = [
    "social_media_toxicity_dataset.json",
    "profanity_dataset.json",
    "twitter_hate_speech_dataset.json",
]

with ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5002") as client:
    for file in list_of_files:
        hash = client.add(file)
        print(hash)

        # write to txt file
        with open("ipfs_hashes.txt", "a") as f:
            f.write(hash["Hash"] + "\n")
