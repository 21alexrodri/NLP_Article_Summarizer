from re import S
from model.nltk_tokenize_class import NLTKTokenizer
from model.spacy_tokenize_class import SpacyTokenizer
from model.article_extractor_class import ArticleExtractor
from model.article_summarizer_class import ArticleSummarizer
from model.topic_classifier_class import TopicClassifier
from model.topic_classifier_class_2 import TopicClassifier2
url = "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded"

# science_article = ArticleExtractor(url)
# print("Title:", science_article.title)
# text = science_article.extract_text_bs4_method()


# summarizer = ArticleSummarizer()
# summary = summarizer.summarize(text)

# print("\nRESUM DE L'ARTICLE:\n")
# print(summary)

print("===================================")
print("| Welcome to the NLP Article Test |")
print("===================================\n")
print(" · This is a simple test of how NLP would works")
print(" · This test includes text extraction, tokenization, thematic classification and article summarization.\n")

print("Please, select an article to analyze:")
print("1 - Grasshopper Genome Expansion")
print("2 - Controversial Offside Leaves Barcelona Fuming")
print("3 - Debunking the Gold vs. Dollar Index Fallacy")
print("4 - Albino gorilla dies in Spain")
print("5 - Journalistic Ingenuity in Spain Train Disaster Coverage")

choice = input("Enter the number of your choice (1-5): ")

article_urls = {
    "1": "https://link.springer.com/article/10.1186/s12915-020-00925-x",
    "2": "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded",
    "3": "https://goldbroker.com/news/fallacy-inverse-relationship-between-gold-dollar-index-dxy-3363",
    "4": "https://www.nbcnews.com/id/wbna3541441",
    "5": "https://www.ap.org/the-definitive-source/behind-the-news/spain-train-crash-how-a-journalists-quick-thinking-led-to-vital-info/"
}

if choice in article_urls:
    url = article_urls[choice]

    print("______________________________\n")
    print("✅✅✅ Url accepted. ✅✅✅")
    print("______________________________\n")


    # Article text extraction
    print("Extracting text step...")
    print("Select the extraction method:")
    print("1 - Newspaper method (default)")
    print("2 - BeautifulSoup method")
    extraction_choice = input("Enter the number of your choice (1-2): ")
    extractor = ArticleExtractor(url)
    if extraction_choice == "1":
        text = extractor.extract_text_newspaper_method()
    elif extraction_choice == "2":
        text = extractor.extract_text_bs4_method()
    else:
        print("❌❌❌ Invalid choice. Using Newspaper method by default. ❌❌❌")
        text = extractor.extract_text_newspaper_method()
    print("✅✅✅ Text extracted successfully. ✅✅✅")

    # Tokenization
    print("\n______________________________\n")
    print("Tokenization step...")
    print("Select the tokenizer:")
    print("1 - NLTK Tokenizer (default)")
    print("2 - SpaCy Tokenizer")
    tokenizer_choice = input("Enter the number of your choice (1-2): ")
    if tokenizer_choice == "1":
        tokenizer = NLTKTokenizer()
    elif tokenizer_choice == "2":
        tokenizer = SpacyTokenizer()
    else:
        print("❌❌❌ Invalid choice. Using NLTK Tokenizer by default. ❌❌❌")
        tokenizer = NLTKTokenizer()

    tokens = tokenizer.clean_tokenize(text)
    print("✅✅✅ Tokenization completed successfully. ✅✅✅")

    # Thematic Classification
    print("\n______________________________\n")
    print("Thematic Classification step...")
    print("Select the classification method:")
    print("1 - Zero-Shot Classification (default)")
    print("2 - Sentence Embedding Classification")
    classification_choice = input("Enter the number of your choice (1-2): ")
    if classification_choice == "1":
        classifier = TopicClassifier()
        classification_result = classifier.classify(text)
    elif classification_choice == "2":
        classifier = TopicClassifier2()
        classification_result = classifier.classify(text)
    
    print("✅✅✅ Thematic Classification completed successfully. ✅✅✅")
    
    # Article Summarization
    print("\n______________________________\n")
    print("Article Summarization step...")
    print("Select the summarization method:")
    print("1 - Raw text (default)")
    print("2 - Tokenized text")
    summarization_choice = input("Enter the number of your choice (1-2): ")
    summarizer = ArticleSummarizer()
    if summarization_choice == "1":
        summary = summarizer.summarize(text)
    elif summarization_choice == "2":
        tokenized_text = ' '.join(tokens)
        summary = summarizer.summarize(tokenized_text)
    
    print("✅✅✅ Article Summarization completed successfully. ✅✅✅")

    print("\n______________________________\n")

    print("🎊🎊🎊 FINAL RESULTS 🎊🎊🎊\n")

    value = -1
    while value != "0":
        print("Select the result to display:")
        print("1 - Article Title")
        print("2 - Article Text")
        print("3 - Tokenized Text")
        print("4 - Thematic Classification")
        print("5 - Article Summary")
        print("0 - Exit")
        value = input("Enter the number of your choice (0-5): ")
        match value:
            case "1":
                print("\n--- Article Title ---")
                print(extractor.title)
            case "2":
                print("\n--- Article Text ---")
                print(text)
            case "3":
                print("\n--- Tokenized Text ---")
                print(tokens)
            case "4":
                print("\n--- Thematic Classification ---")
                for label, score in zip(classification_result['labels'], classification_result['scores']):
                    print(f"{label:<40}: {score:.4f}")
            case "5":
                print("\n--- Article Summary ---")
                print(summary)
            case "0":
                print("Exiting the program. Goodbye!")
            case _:
                print("❌❌❌ Invalid choice. Please try again. ❌❌❌")

    


    
else:
    print("❌❌❌ Invalid choice. Exiting the program. ❌❌❌")




# tokenizer = SpacyTokenizer()
# tokens = tokenizer.clean_tokenize(text)
# print(tokens)


