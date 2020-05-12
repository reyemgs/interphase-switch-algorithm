%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  BBA source codes version 1.1                                     %
%  Developed in MATLAB R2011b(7.13)                                 %
%  Author and programmer: Seyedali Mirjalili                        %
%         e-Mail: ali.mirjalili@gmail.com                           %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Main source code :
% ======================================================== % 
% Files of the Matlab programs included in the book:       %
% Xin-She Yang, Nature-Inspired Metaheuristic Algorithms,  %
% Second Edition, Luniver Press, (2010).   www.luniver.com %
% ======================================================== %    

% -------------------------------------------------------- %
% Bat-inspired algorithm for continuous optimization (demo)%
% Programmed by Xin-She Yang @Cambridge University 2010    %
% -------------------------------------------------------- %

function [best,fmin,cg_curve]=BBA(n, A, r, d, Max_iter, CostFunction, kodV)
    %     best - двоичный вектор подключений ОП, для которого получено лучшее F
    %     fmin - само лучшее значение целевой функции F
    % cg_curve - вектор лучших значений на каждой итерации/кривая сходимости
    
    %            n - размер популяции (обычно от 10 до 25)
    %            d - длина оптимизируемого бинарного вектора
    %     Max_iter - максимальное количество итераций
    % CostFunction - функция цели (оценочная функция)
    %            A - значение громкости  (свободный параметр)
    %            r - значение часторы (свободный параметр)
    
    % Этот частотный диапазон определяет масштабирование
    Qmin=0;         % Минимальная частота
    Qmax=2;         % Максимальная частота
    
    % Итерационные параметры
    N_iter=1;       % Общее количество оценок функций
    
    % Инициализация массивов
    Q=zeros(n,1);   % Частоты
    v=zeros(n,d);   % Скорости
    Sol=zeros(n,d);
    cg_curve=zeros(1,Max_iter);
    
        % Инициализация популяции/решений
        for i=1:n,
            for j=1:d % для измерения
                if rand<=0.5
                    Sol(i,j)=0;
                else
                    Sol(i,j)=1;
                end
            end
        end
    
        %% вброс исходной комбинации
        Sol(1,:) = kodV;
        %% -------------------------
        
        for i=1:n,
            Fitness(i)=CostFunction(Sol(i,:));
        end
    
        % Поиск текущего лучшего
        [fmin,I]=min(Fitness);
        best=Sol(I,:);
        cg_curve(1) = fmin; % это моя коррекция
        
        % ======================================================  %
        % Примечание: в данной версии не реализовано уменьшение   %
        % громкости и увеличение скорости излучения.              %
        % ======================================================  %
    
        % Начало итераций -- Binary Bat Algorithm
        while (N_iter<(Max_iter))
                % Перебираем всех мышей/решения
                N_iter=N_iter+1;
                cg_curve(N_iter)=fmin;
                for i=1:n,
                    for j=1:d
                        Q(i)=Qmin+(Qmin-Qmax)*rand; % Уравнение 3 в статье
                        v(i,j)=v(i,j)+(Sol(i,j)-best(j))*Q(i); % Уравнение 1 в статье
    
                        V_shaped_transfer_function=abs((2/pi)*atan((pi/2)*v(i,j))); % Уравнение 9 в статье
    
                        if rand<V_shaped_transfer_function % Уравнение 10 в статье
                            Sol(i,j)=~Sol(i,j);
                        else
                            Sol(i,j)=Sol(i,j);
                        end
    
                        if rand>r  % значение частоты пульсации
                              Sol(i,j)=best(j);
                        end   
    
                    end       
    
                   Fnew=CostFunction(Sol(i,:)); % Оцениваем новые решения
    
                   if (Fnew<=Fitness(i)) && (rand<A)  % Если решение улучшится или не слишком громко
                        Sol(i,:)=Sol(i,:);
                        Fitness(i)=Fnew;
                   end
    
                  % Обновить текущее лучшее
                  if Fnew<=fmin,
                        best=Sol(i,:);
                        fmin=Fnew;
                  end
    
                end
    
        end
    
    end