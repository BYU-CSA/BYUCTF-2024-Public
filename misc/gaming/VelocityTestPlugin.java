package com.github.byu-csa.VelocityTestPlugin;

import com.google.inject.Inject;
import com.velocitypowered.api.event.Subscribe;
import com.velocitypowered.api.event.query.ProxyQueryEvent;
import com.velocitypowered.api.plugin.Plugin;
import com.velocitypowered.api.proxy.ProxyServer;
import com.velocitypowered.api.proxy.server.QueryResponse;

import java.lang.reflect.Proxy;

import org.slf4j.Logger;

@Plugin(id = "velocity-ctf", name = "A BYU CTF challenge", version = "0.1.0-SNAPSHOT",
        url = "https://cybersecurity.byu.edu/csa", description = "An amazing challenge", authors = {"Me"})
public class VelocityTestPlugin {
    private final ProxyServer server;
    private final Logger logger;


    @Inject
    public VelocityTestPlugin(ProxyServer server, Logger logger) {
        this.server = server;
        this.logger = logger;
    }

    @Subscribe
    public void onQuery(ProxyQueryEvent event) {
        if (event.getQueryType() == ProxyQueryEvent.QueryType.BASIC) {
            event.setResponse(event.getResponse().toBuilder().hostname("byuctf{th1s!s@Gr8tgam3}").plugins(QueryResponse.PluginInformation.of("BYU CTFs", "0.0.1")).build());
        }
    }
}
