<%@ page contentType="text/html; charset=UTF-8" %>
            <%@ taglib prefix="s" uri="/struts-tags" %>
            <nav class="navbar navbar-custom navbar-fixed-top">
                <div class="container">
                    <div class="navbar-header">
                        <s:url action="home" var="home" escapeAmp="false" namespace="/" />
                        <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#custom-collapse"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button><a class="navbar-brand" style="padding-top:5px; padding-bottom:5px" href="<s:property value="#home" />"><img src="/assets/images/logo.png" alt="wyca-analytics"/></a>
                    </div>
                    <div class="collapse navbar-collapse" id="custom-collapse">
                        <ul class="nav navbar-nav navbar-right">
                            <s:if test="#session.user != null">
                                
                                <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN)">
                                    <li class="dropdown">
                                        <s:url action="list" var="url100" escapeAmp="false" namespace="/posts" />
                                        <a class="dropdown-toggle" href="<s:property value="#url100" />" data-toggle="dropdown">Blog</a>
                                        <ul class="dropdown-menu">
                                            <li>
                                                <s:url action="new" var="url101" escapeAmp="false" namespace="/post-admin" />
                                                <a href="<s:property value="#url101" />">neuer Post</a>
                                            </li>
                                            <li>
                                                <s:url action="list" var="url102" escapeAmp="false" namespace="/post-admin" />
                                                <a href="<s:property value="#url102" />">Posts bearbeiten</a>
                                            </li>
                                            <li>
                                                <s:url action="image-list" var="url103" escapeAmp="false" namespace="/post-admin" />
                                                <a href="<s:property value="#url103" />">Bilder verwalten</a>
                                            </li>
                                        </ul>
                                    </li>
                                </s:if>
                                <s:else>
                                    <s:url action="list" var="url10" escapeAmp="false" namespace="/posts" />
                                    <li><a href="<s:property value="#url10" />">Blog</a></li>
                                </s:else>

                                <!-- market -->
                                <li class="dropdown">
                                    <s:url action="yc" var="market_100" escapeAmp="false" namespace="/market" />
                                    <a href="<s:property value="#market_100" />" class="dropdown-toggle" data-toggle="dropdown"><s:text name="navigation.market" /></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="<s:property value="#market_100" />"><s:text name="navigation.market.main" /></a></li>
                                        <s:url action="SP500" var="market_101" escapeAmp="false" namespace="/market-breadth" />
                                        <li><a href="<s:property value="#market_101" />"><s:text name="navigation.marketbreadth" /></a></li>
                                        <s:url action="yieldrates" var="yr" escapeAmp="false" namespace="/bonds" />
                                        <li><a href="<s:property value=" #yr"/>"><s:text name="navigation.market.yieldrates" /></a></li>

                                        <li>----------------</li>
                                        <s:url action="NYSE" var="md_nyse" escapeAmp="false" namespace="/market-diary" />
                                        <li><a href="<s:property value=" #md_nyse"/>"><s:text name="navigation.market.market-diary" /></a></li>
                                        <s:iterator value="%{#session.markets}">
                                            <li>
                                                <s:set var="market"><s:property /></s:set>
                                                <s:url action="%{market}" var="marketURL" escapeAmp="false" namespace="/market-detail" />
                                                <a href="<s:property value="#marketURL" />"><s:property value="displayName" /></a>
                                            </li>
                                        </s:iterator>

                                        <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN) || #session.user.role.equals(@com.stevwyman.jasmin.access.Role@PREMIUM)">
                                            <li>----------------</li>
                                            <li><a href="/market/strength" /><s:text name="navigation.market.strength" /></a></li>
                                            <li><a href="/shorts/list-view" /><s:text name="navigation.market.shorts.de" /></a></li>
                                            <li><a href="/openinterest" /><s:text name="navigation.market.openinterest" /></a></li>
                                            <li><a href="/seasonality" />Seasonality</a></li>
                                            <s:url action="overview" var="sentiment_overview" escapeAmp="false" namespace="/sentiment" />
                                            <li><a href="<s:property value=" #sentiment_overview " />">Sentiment</a></li>
                                            <li><a href="/boom-crisis.htm" />Boom - Crisis</a></li>
                                            <s:url action="sectors" var="market_sector" escapeAmp="false" namespace="/market" />
                                                <li><a href="<s:property value="#market_sector"/>" /><s:text name="navigation.market.overview" /></a></li>
                                            <s:url action="pre-market" var="pm" escapeAmp="false" namespace="/mobile" />
                                                <li><a href="<s:property value="#pm"/>">US pre-market</a></li>
                                        </s:if>
                                        <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN) || #session.user.role.equals(@com.stevwyman.jasmin.access.Role@PREMIUM) || #session.user.role.equals(@com.stevwyman.jasmin.access.Role@BASIC)">
                                            <li>----------------</li>
                                            <li><a href="/bonds/tips" /><s:text name="navigation.market.tips" /></a></li>
                                        </s:if>
                                    </ul>
                                </li>

                                <li class="dropdown">
                                    <s:url action="SP500" var="url131" escapeAmp="false" namespace="/overview" />
                                    <a href="<s:property value="#url131" />" class="dropdown-toggle" data-toggle="dropdown"><s:text name="navigation.watchlist" /></a>
                                    <ul class="dropdown-menu">
                                        <li>
                                            <a href="<s:property value="#url131" />"><s:text name="navigation.watchlist.start" /></a>
                                        </li>
                                        <s:if test="#session.user != null">
                                                <li>----------------</li>
                                            <s:iterator value="%{#session.watchlists}">
                                                <li>
                                                    <s:url action="interval-view" var="watchlistView" escapeAmp="false" namespace="%{localDataProvider.watchlistNameSpace}" >
                                                        <s:param name="id"><s:property value="id" /></s:param>
                                                        <s:param name="interval">DAILY</s:param>
                                                    </s:url>
                                                    <a href="<s:property value=" #watchlistView " />"><s:property value="name" /></a>
                                                </li>
                                            </s:iterator>
                                        </s:if>
                                    </ul>
                                </li>

                                <li class="dropdown">
                                    <s:url action="overview" var="url14" escapeAmp="false" namespace="/filter" />
                                    <a href="<s:property value="#url14" />" class="dropdown-toggle" data-toggle="dropdown"><s:text name="navigation.filter" /></a>
                                    <ul class="dropdown-menu">
                                        <li>
                                            <s:url action="indicator" var="url141" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url141" />"><s:text name="navigation.screener.filter.indicator" /></a>
                                        </li>
                                        <li>
                                            <s:url action="signal" var="url141a" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url141a" />"><s:text name="navigation.screener.filter.signal" /></a>
                                        </li>
                                        <li>
                                            <s:url action="strength" var="url142" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url142" />"><s:text name="navigation.screener.filter.strength" /></a>
                                        </li>
                                        <li>
                                            <s:url action="candlestick" var="url143" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url143" />"><s:text name="navigation.screener.filter.candlestick" /></a>
                                        </li>
                                        <li>
                                            <s:url action="trend" var="url144" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url144" />"><s:text name="navigation.screener.filter.trend" /></a>
                                        </li>
                                        <li>
                                            <s:url action="fundamentals" var="url145" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url145" />"><s:text name="navigation.screener.filter.fundamentals" /></a>
                                        </li>
                                        <li>
                                            <s:url action="geometric-pattern" var="url146" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url146" />"><s:text name="navigation.screener.filter.geometric" /></a>
                                        </li>
                                        <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN) || #session.user.role.equals(@com.stevwyman.jasmin.access.Role@PREMIUM)">
                                        <li>
                                            <s:url action="attributes" var="url147" escapeAmp="false" namespace="/filter" />
                                            <a href="<s:property value="#url147" />"><s:text name="navigation.screener.filter.attributes" /></a>
                                        </li>
                                        </s:if>
                                    </ul>
                                </li>

                                <li class="dropdown">
                                    <s:url action="screener-overview" var="url15" escapeAmp="false" namespace="/watchlist" />
                                    <a href="<s:property value="#url15" />" class="dropdown-toggle" data-toggle="dropdown"><s:text name="navigation.screener" /></a>
                                    <ul class="dropdown-menu">
                                        <s:iterator value="%{#session.watchlists}">
                                            <li>
                                                <s:url action="screener-view" var="screenerView" escapeAmp="false" namespace="/watchlist" >
                                                    <s:param name="id"><s:property value="id" /></s:param>
                                                    <s:param name="interval">DAILY</s:param>
                                                </s:url>
                                                <a href="<s:property value=" #screenerView " />"><s:property value="name" /></a>
                                            </li>
                                        </s:iterator>
                                    </ul>
                                </li>

                                <li class="dropdown">
                                    <a href="/start" title="start"><i class="fa fa-fw">&#xF0E4;</i></a>
                                    <ul class="dropdown-menu">

                                        <s:url action="screener-settings" var="url141" escapeAmp="false" namespace="/" />
                                        <li><a href="<s:property value="#url141" />"><s:text name="navigation.settings" /></a></li>

                                        <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN) || #session.user.role.equals(@com.stevwyman.jasmin.access.Role@PREMIUM)">
                                            <li>----------------</li>
                                            <li>
                                                <s:url action="DAX40" var="market_my_view" escapeAmp="false" namespace="/market-analysis" />
                                                <a href="<s:property value="#market_my_view" />">My Market View</a>
                                            </li>
                                            <li>
                                                <s:url action="view" var="urlDerivativesPortfolio" escapeAmp="false" namespace="/derivatives" />
                                                <a href="<s:property value="#urlDerivativesPortfolio" />">D | Portfolio</a>
                                            </li>
                                            <li>
                                                <s:url action="limit-overview" var="url132" escapeAmp="false" namespace="/limit" />
                                                <a href="<s:property value="#url132" />"><s:text name="navigation.limitOverview" /></a>
                                            </li>
                                            <li>
                                                <s:url action="alarm-overview" var="url133" escapeAmp="false" namespace="/limit" />
                                                <a href="<s:property value="#url133" />"><s:text name="navigation.alarmOverview" /></a>
                                            </li>
                                            <li>
                                                <s:url action="list-watchlists" var="url134" escapeAmp="false" namespace="/settings" />
                                                <a href="<s:property value="#url134" />"><s:text name="navigation.settings" /></a>
                                            </li>
                                        </s:if>

                                        <s:if test="#session.user.role.equals(@com.stevwyman.jasmin.access.Role@ADMIN)">
                                            <s:url action="system-management" var="url143" escapeAmp="false" namespace="/nimad" />
                                            <li><a href="<s:property value="#url143" />">Sys Mgmt</a></li>
                                        </s:if>

                                        <s:url action="sign-out" var="url142" escapeAmp="false" namespace="/auth" />
                                        <li><a href="<s:property value="#url142" />" title="<s:text name="navigation.logout" />"><i class="fa fa-fw">&#xF08B;</i></a></li>
                                    </ul>
                                </li>
                            </s:if>
                            <s:else>
                                <!-- login -->
                                <li>
                                    <s:url action="sign-in" var="url140" escapeAmp="false" namespace="/" />
                                    <a href="<s:property value="#url140" />" title="<s:text name="navigation.loginregister" />"><i class="fa fa-fw">&#xF090;</i></a>
                                </li>
                            </s:else>

                                <!-- language -->
                                <li class="dropdown">
                                    <s:if test='locale.toString() == "en_GB" '>
                                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><img src="/assets/images/blank.gif" class="flag flag-gb" alt="gb" /></a>
                                    </s:if>
                                    <s:elseif test='locale.toString() == "de_DE" '>
                                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><img src="/assets/images/blank.gif" class="flag flag-de" alt="de" /></a>
                                    </s:elseif>
                                    <s:else>
                                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><img src="/assets/images/blank.gif" class="flag flag-us" alt="us" /></a>
                                    </s:else>

                                    <ul class="dropdown-menu">
                                        <s:url var="urlus" includeParams="all" value="">
                                            <s:param name="request_locale">en_US</s:param>
                                        </s:url>
                                        <li>
                                            <s:a href="%{urlus}"><img src="/assets/images/blank.gif" class="flag flag-us" alt="us" /></s:a>
                                        </li>
                                        <s:url var="urlen" includeParams="all" value="">
                                            <s:param name="request_locale">en_GB</s:param>
                                        </s:url>
                                        <li>
                                            <s:a href="%{urlen}"><img src="/assets/images/blank.gif" class="flag flag-gb" alt="en" /></s:a>
                                        </li>
                                        <s:url var="urlde" includeParams="all" value="">
                                            <s:param name="request_locale">de_DE</s:param>
                                        </s:url>
                                        <li>
                                            <s:a href="%{urlde}"><img src="/assets/images/blank.gif" class="flag flag-de" alt="de" /></s:a>
                                        </li>
                                    </ul>
                                </li>

                        </ul>
                    </div>
                </div>
            </nav>
