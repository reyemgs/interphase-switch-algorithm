function [ output_Vect ] = Korrection( input_Vect, PreviousVect )
    %% Корректируемрасчётный вектор input_Vect - заменяем "11" на "как было" у предыдущего лучшего
        N = length(input_Vect);
        for z = 1:2:N
            if input_Vect(z)==1 & input_Vect(z+1)==1 
                input_Vect(z) = PreviousVect(z);
                input_Vect(z+1) = PreviousVect(z+1);
            end
        end
        output_Vect = input_Vect;
    end
    
    