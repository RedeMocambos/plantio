<template>
    <v-form
        v-model="valid"
    >
        <v-card
            class="pl-3"
        >
            <v-card-title>
                <div class="headline">
                    {{ textoCabecalho }}
                </div>
            </v-card-title>
            <v-text-field
                v-model="dadosArea.nome"
                label="Nome"
                @change="atualizarCampo('nome', $event)"
            />
            <v-select
                v-model="dadosArea.localidade_id"
                :items="listaLocalidades"
                item-text="nome"
                item-value="id"
                label="Localidade"
                @change="atualizarCampo('localidade_id', $event); atualizarCampoMatriz('localidade', $event, listaLocalidades)"
            />
            <v-text-field
                v-model="dadosArea.dimensao"
                label="Dimensão"
                @change="atualizarCampo('dimensao', $event)"
            />
            <v-text-field
                v-model="dadosArea.largura"
                label="Largura"
                @change="atualizarCampo('largura', $event)"
            />
            <v-text-field
                v-model="dadosArea.comprimento"
                label="comprimento"
                @change="atualizarCampo('comprimento', $event)"
            />
        </v-card>
        <v-card
            class="pa-3"
        >
            <v-select
                v-model="dadosArea.solo_predominante"
                :items="dadosAreaMetadata.solo"
                item-text="descricao"
                item-value="valor"
                label="Solo predominante"
                @change="atualizarCampo('Solo predominante', $event)"
            />
            <v-select
                v-model="dadosArea.declividade_predominante"
                :items="dadosAreaMetadata.declividade"
                item-text="descricao"
                item-value="valor"
                label="Declividade predominante"
                @change="atualizarCampo('declividade_predominante', $event)"
            />
            <v-select
                v-model="dadosArea.microclima"
                :items="dadosAreaMetadata.microclimas"
                item-text="descricao"
                item-value="valor"
                label="Microclima"
                @change="atualizarCampo('microclima', $event)"
            />
        </v-card>
        <v-btn
            color="info"
            @click="salvar()"
        >
            <v-icon
                class="pr-3"
            >save</v-icon>
            salvar
        </v-btn>
        <v-btn
            color="error"
            @click="voltar()"
        >
            <v-icon
                class="pr-3"
            >cancel</v-icon>
            cancelar
        </v-btn>
    </v-form>
</template>
<script>
import Tools from '@/mixins/tools';
import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'FormEditarArea',
    mixins: [
        Tools,
    ],
    props: {
        textoCabecalho: {
            type: String,
            default: 'Edição de área',
        },
        tipo: {
            type: String,
            default: 'editar',
        },
    },
    data() {
        return {
            valid: true,
            dadosEditados: {
                id: '',
                nome: '',
                dimensao: '',
                largura: '',
                comprimento: '',
                solo_predominante: '',
                declividade_predominante: '',
                localidade_id: 0,
                localidade: '',
                microclima: '',
            },
        };
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
            listaLocalidades: 'localidade/localidades',
            dadosAreaMetadata: 'area/getAreaMetadata',
        }),
    },
    watch: {
        dadosArea() {
            this.inicializarDadosArea();
        },
    },
    created() {
        this.inicializarDadosArea();
    },
    methods: {
        ...mapActions({
            adicionarArea: 'area/adicionarArea',
            updateArea: 'area/updateArea',
        }),
        inicializarDadosArea() {
            this.dadosEditados = {
                id: this.dadosArea.id,
                nome: this.dadosArea.nome,
                dimensao: this.dadosArea.dimensao,
                largura: this.dadosArea.largura,
                comprimento: this.dadosArea.comprimento,
                solo_predominante: this.dadosArea.solo_predominante,
                declividade_predominante: this.dadosArea.declividade_predominante,
                localidade_id: this.dadosArea.localidade_id,
                localidade: this.dadosArea.localidade,
                microclima: this.dadosArea.microclima,
            };
        },
        atualizarCampo(key, value) {
            if (Object.keys(this.dadosEditados).includes(key)) {
                this.dadosEditados[key] = value;
            }
        },
        atualizarCampoMatriz(key, value, lista) {
            const campo = lista.find(obj => obj.id === value);
            return campo.nome;
        },
        salvar() {
            if (this.tipo === 'criar') {
                this.adicionarArea(this.dadosEditados)
                    .then((response) => {
                        const path = `/area/${response.id}/editar`;
                        this.$router.push({ path });
                    });
            } else if (this.tipo === 'editar') {
                this.updateArea(this.dadosEditados);
            }
        },        
    },
};
</script>
