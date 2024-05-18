from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

flag = 'nah lol'

def load_models():
    conservative_model = Doc2Vec.load("conservative_model.d2v")
    liberal_model = Doc2Vec.load("liberal_model.d2v")
    return conservative_model, liberal_model

def predict(comment, model_conservative, model_liberal):
    tokens = word_tokenize(comment)

    new_vector_conservative = model_conservative.infer_vector(tokens)
    new_vector_liberal = model_liberal.infer_vector(tokens)

    similar_coms_conservative = model_conservative.dv.most_similar([new_vector_conservative], topn=len(model_conservative.dv))
    similar_coms_liberal = model_liberal.dv.most_similar([new_vector_liberal], topn=len(model_liberal.dv))

    sim_conservative = sum(float(similarity) for _, similarity in similar_coms_conservative) / len(similar_coms_conservative)
    sim_liberal = sum(float(similarity) for _, similarity in similar_coms_liberal) / len(similar_coms_liberal)

    total_sim = sim_conservative + sim_liberal
    sim_conservative = sim_conservative / total_sim
    sim_liberal = sim_liberal / total_sim

    if sim_conservative >= 1 or sim_liberal >= 1:
        print("Hmmmm, that doesn't seem right...")
        print(flag)

    print(sim_liberal)
    print(sim_conservative)

    if sim_conservative > sim_liberal:
        print(f'Comment is Conservative: ({round(sim_conservative * 100)}% confidence)')
    else:
        print(f'Comment is Liberal: ({round(sim_liberal * 100)}% confidence)')

if __name__ == '__main__':
    conservative_model, liberal_model = load_models()

    while True:
        comment = input('Input a comment to test: ')
        newcomment = ''
        for letter in comment:
            if letter == ' ':
                pass
            else:
                newcomment += letter
        if newcomment:
            predict(comment, conservative_model, liberal_model)

