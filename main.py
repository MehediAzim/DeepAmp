import argparse
import read
import generateBPF
import predict
import numpy as np

def main(args):
    
    sequences, label = read.fetchXY(args.fasta, args.label)
    print('\nDatasets fetching done.')

    ############################################################################
    print('Features extraction begins. Be patient! The machine will take some time.')

    feature = generateBPF.extract_feature(sequences)
    print(feature.shape)

    predict.classifier(feature, label, args)
    

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from Peptide Sequences')

    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='AMPylation_data.fsa')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='label.txt')

    args = p.parse_args()

    main(args)
