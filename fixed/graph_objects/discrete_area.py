def discrete_area(x,y,*args,**keywords):
    '''
    example:
    fig = make_subplots()
    plotly_obj=discrete_area(x=time,y=EPA['PM2_5'],name='PM<sub>2.5</sub> &#9;&#9;',legendgroup='PM',
        line={'color':plotly_get_color(count)}),
    for pg in plotly_obj[0]:
        fig.add_trace(pg,row=1,col=1,secondary_y=True,)
    '''

    nullnum = np.where(y==None)[0] if None in y else np.where(np.isnan(y)[0])
    nullspace_lb=(nullnum-1).tolist()
    samespace=list(set(nullspace_lb).intersection(set(nullnum)))
    for e in samespace:
        nullspace_lb.remove(e)

    nullspace_ub=(nullnum+1).tolist()
    samespace=list(set(nullspace_ub).intersection(set(nullnum)))
    for e in samespace:
        nullspace_ub.remove(e)

    nullspace=nullspace_lb+nullspace_ub
    # nullspace=list(set((nullnum-1).tolist()+(nullnum+1).tolist()))
    # samespace=list(set(nullspace).intersection(set(nullnum)))
    # for e in samespace:
    #     nullspace.remove(e)
    nullspace.sort()
    if not len(y)-1 in nullspace: nullspace.append(len(y)-1) 
    bool_plot = False if 0 in nullspace else True
    if bool_plot: nullspace=[0]+nullspace
    
    trace=[]
    toggleLegend = True
    for i in range(len(nullspace)-1):
        if bool_plot:
            trace.append(go.Scatter(
                x=x[nullspace[i]:nullspace[i+1]+1],
                y=y[nullspace[i]:nullspace[i+1]+1],
                mode='lines',
                fill='tozeroy',
                showlegend=toggleLegend,
                **keywords
            ))
            toggleLegend=False
        bool_plot=not bool_plot
    return trace

