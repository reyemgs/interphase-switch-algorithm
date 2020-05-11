%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Общий файл MainAll - version 1.1                                 %
%  Подготовлен в MATLAB 2015                                        %
%  Разработчик: Василий Мохов                                       %
%         email: mokhov_v@mail.ru                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clc % очистка консоли
close all;         % закрыть все открытые графики
for col_OP = 3:30
save('result/count.mat', 'col_OP');
clear all;         % очистить память 
load('result/count.mat', 'col_OP');
warning off

%% Задаём исходные данные
global col_OP;              % Количество однофазных пользователей
%       col_OP = 30;        % определяется пользователем
Max_iteration = 30;         % Количечтво итераций (повторений/эпох) алгоритма
          noP = 25;         % Количество агентов (мышей, частиц и т.п.)
global noV;                 % Количество бинарных переменных 
%         noV = col_OP*2;   % всегда = col_OP*2                    
    Count_OSC = 56;         % Количество используемых оциллограмм (из 56)
global Izm;                 % Массив осциллограмм размерности Count_OSC
%global MyConvergenceCurve; % общий массив значений целевой функции
global StartSum;            % значения сумм токов по фазам для исходной комбинации
global StartTHD;            % и значения THD по фазам для исходной комбинации
AlgName = 'BBA';            % Название ипытуемого алгоритма

%% Формируем массив измерений (массив осциллограмм)
% из файлов с именами osc_best/I1.txt, osc_best/I2.txt, osc_best/I3.txt,...
Izm = zeros(Count_OSC,104);
for i=1:Count_OSC 
    s = strcat('osc_best/I', int2str(i), '.txt'); % формируем имя файла
    Izm(i,:) = dlmread(s);                        % пишем в i-й массив
end

%% Загружаем структуру SamplesV
load('samples/V.mat', 'SamlesV');
global V;           % структура с исходными данными для расчетов
kodV = [];        % двоичный код вектора подключений ОП
% создаем структуру для записи результатов
RES(1:100) = struct('Y_N',0,'Time',0,'Fbest',0,'Fsteps',0,'FinVect',0,...
             'RasprOP',0,'KpOP',0,'Fmean',0,'Fvar',0,'YoK',0);
    %     Y_N - признак улучшения результата на 10%
    %    Time - время работы алгоритма в секундах
    %   Fbest - лучшее найденное решение - F(X)
    %  Fsteps - траектория поиска по эпохам (вектор сходимости)
    % FinVect - двоичный вектор лучшего найденного распределения ОП - X
    % RasprOP - лучшее найденное распределения ОП
    %    KpOP - количество переключений ОП
    %   Fmean - оценка математического ожидания на 100 прмерах
    %    Fvar - оценка дисперсии на 100 примерах
    %     YoK - процент положительных результатов из 100 примеров
    %           с одинаковым числом однофазных пользователей    
% ---->
    disp(['Считаю для КОП = ',num2str(col_OP),', время ',datestr(now)]);
    noV = col_OP*2; % количество бинарных переменных
    V = [];
    BestsF = [];
    Y = 0;
        %% Формируем указатель на оценочную функцию (функцию цели)
        CostFunction=@(x) MyCost(x); % Код функциив файле Mycost.m
        %%  на функцию расчёта суммы токов и THD по фазам
        Sum_THD=@(Vx) Calc_sum_thd(Vx); % Код функциив файле Calc_sum_thd.m
        %% на функцию алгоритма
        SwAlg=@(n, A, r, d, Max_iter, CostFunction, kodV) BBA(n, A, r, d, Max_iter, CostFunction, kodV);
%% цикл обработки 100 примеров
for j = 1:1
    varlist = {'A', 'c', 'ConvergenceCurve',...
           'FinSum', 'FinSumOsc', 'FinTHD',...
           'gBest','gBestScore','i', 'kodV',...
           'per', 'PreviousBest', 'PreviousV', 'r',...
           'Raspr_OP', 's','ss', 'Startf1', 'Startf2',...
           'StartKPOP','StartScore','StartSumOsc'};
    clear(varlist{:})
            kodV = []; 
            disp(['Пример = ',num2str(j)]);
            % выбираем i-й вектор номеров осциллограм для ОП
            V(2,:) = SamlesV(col_OP).V2(j,:);
            % выбираем i-й вектор случайного рапределения ОП пофазам
            V(3,:) = SamlesV(col_OP).V3(j,:);
            % выбираем i-й двоичный код вектора случайного рапределения ОП пофазам
            kodV  =  SamlesV(col_OP).kV(j,:);

            %% Ввычисляем значения StartSum, StartTHD и целевой функции для исходной комбинации
                [StartSum, StartTHD, StartKPOP, ~, StartSumOsc] = Sum_THD(kodV);
                % корректируем THD, если оно не определено (т.е. I=0)
                 StartTHD(isnan(StartTHD))=[100];
                % значение целевой функции для начальной комбинации
                StartScore = CostFunction(kodV);
                % Вычисляем элементы для целевой функции для начальной комбинации
                [~, Startf1, Startf2, ~] = Calc_Fitness(StartSum, StartTHD, StartKPOP);

            %% Задаём код начального "предыдущего" лучшего вектора подключений ОП
            %  и значение оценочной функции для него
            global PreviousV PreviousBest;
                PreviousV = kodV;
                PreviousBest = StartScore;

            %% -1- Запускаем алгоритм AlgName
                    A=.25;      % Значение громкости  (constant or decreasing)
                    r=.1;       % Значение часторы (constant or decreasing)
                 TimeStart = tic;
                    [gBest, gBestScore, ConvergenceCurve] = SwAlg(noP, A, r, noV, Max_iteration, CostFunction, kodV);
                 TimeElapsed = toc(TimeStart);
                    gBest = Korrection( gBest, PreviousV );
                 ConvergenceCurve = ConvergenceCurve/StartScore; % нормируем значения шагов алгоритма в пределах от 0 до 1

            %% Вычиляем параметры лучшего решения
              [FinSum, FinTHD, per, Raspr_OP, FinSumOsc] = Sum_THD(gBest);

              BestsF(j) = gBestScore/StartScore; % нормирование полученного результата
              % анализ признака улучшения результата на 10%
              if BestsF(j)<=0.9
                  RES(j).Y_N = 1;
                  Y = Y + 1;
              else
                  RES(j).Y_N = 0;
              end
        %% Формируем структуру для сохранения
        RES(j).Time    = TimeElapsed; % время работы алгоритма в секундах
        RES(j).Fbest   = BestsF(j);   % лучшее найденное решение - F(X)
        RES(j).Fsteps  = ConvergenceCurve; % траектория поиска по эпохам (вектор сходимости)
        RES(j).FinVect = gBest;       % двоичный вектор лучшего найденного распределения ОП - X
        RES(j).RasprOP = Raspr_OP;    % лучшее найденное распределения ОП
        RES(j).KpOP    = per;         % количество переключений ОП

end
%% Вычисляем матожидание и дисперсию
RES(1).Fmean = mean(BestsF); % оценка математического ожидания на 100 прмерах
RES(1).Fvar  = var(BestsF);  % оценка дисперсии на 100 примерах
RES(1).YoK   = Y;            % процент положительных результатов из 100 примеров
                             % с одинаковым числом однофазных пользователей
disp(['      Закончил = ',num2str(col_OP),', время ',datestr(now)]);
ss = strcat('result/BBA_', int2str(col_OP), '.mat');
save(ss, 'RES');
end
disp('Время выполнения алгоритма: ');
disp(RES(j).Time);
disp('Лучшее найденное решение - F(X): ');
disp(RES(j).Fbest);
disp('Траектория поиска по эпохам (вектор сходимости): ');
disp(RES(j).Fsteps);
disp('Двоичный вектор лучшего найденного распределения ОП - X: ');
disp(RES(j).FinVect);
disp('Лучшее найденное распределение ОП: ');
disp(RES(j).RasprOP)
disp('Количество переключений: ');
disp(RES(j).KpOP);
warning on