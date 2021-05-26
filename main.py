import argparse
import read
import generateBPF
import predict
import numpy as np


def main(args):
    
    X, Y = read.fetchXY(args.fasta, args.label)
    print('\nDatasets fetching done.')

    ############################################################################
    print('Features extraction begins. Be patient! The machine will take some time.')

    data = generateBPF.extract_feature(args, X, Y)

    feature = data[:, :-1]
    label = data[:, -1]
    # print(T.shape)

    predict.classifier(feature, label, args)

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from DNA Sequences')

    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='AMPylation_1.fsa')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='Label.txt')

    # p.add_argument('-cv', '--nFCV', type=int, help='Number of crossValidation', default=10)

    args = p.parse_args()

    main(args)